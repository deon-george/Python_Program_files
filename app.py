"""
Mobile Camera & Microphone Access via Web Browser
--------------------------------------------------
Run this on your computer/server, then open the URL on your mobile phone.
Both devices must be on the same WiFi network.

Install: pip install flask
Run:     python app.py
Open:    http://<your-computer-ip>:5000  (on your phone's browser)
"""

from flask import Flask, render_template_string
import socket

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Camera & Mic Access</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Courier New', monospace;
    background: #0a0a0a;
    color: #00ff88;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  @keyframes sparkleFlow {
    0% { background-position: 200% center; }
    100% { background-position: -200% center; }
  }

  h1 {
    font-size: 1.4rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin: 20px 0 8px;
    background: linear-gradient(90deg, #00ff88 0%, #ffffff 25%, #00ff88 50%, #ffffff 75%, #00ff88 100%);
    background-size: 200% auto;
    color: transparent;
    -webkit-background-clip: text;
    background-clip: text;
    animation: sparkleFlow 3s linear infinite;
    filter: drop-shadow(0 0 8px rgba(0, 255, 136, 0.4));
  }

  .subtitle {
    font-size: 0.75rem;
    color: #00cc6a;
    letter-spacing: 0.1em;
    margin-bottom: 24px;
  }

  #videoContainer {
    position: relative;
    width: 100%;
    max-width: 480px;
    border-radius: 4px;
    overflow: hidden;
    border: 1px solid #222;
    background: #111;
    aspect-ratio: 4/3;
  }

  video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transform: scaleX(-1); /* mirror selfie cam */
  }

  #overlay {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: #111;
    transition: opacity 0.4s;
  }

  #overlay.hidden { opacity: 0; pointer-events: none; }

  #overlay p { color: #00cc6a; font-size: 0.85rem; }

  .controls {
    display: flex;
    gap: 12px;
    margin-top: 16px;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    max-width: 480px;
  }

  button {
    flex: 1;
    min-width: 120px;
    padding: 12px 16px;
    border: 1px solid #005522;
    background: #141414;
    color: #00ff88;
    font-family: 'Courier New', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.08em;
    cursor: pointer;
    border-radius: 3px;
    transition: all 0.2s;
  }

  button:hover { border-color: #00ff88; color: #00ff88; }
  button:disabled { opacity: 0.3; cursor: not-allowed; }
  button.active { border-color: #ff4444; color: #ff4444; background: #1a0000; }

  #status {
    margin-top: 16px;
    font-size: 0.75rem;
    color: #00cc6a;
    letter-spacing: 0.08em;
    min-height: 1.2em;
    text-align: center;
  }

  #vuMeter {
    width: 100%;
    max-width: 480px;
    margin-top: 12px;
    height: 6px;
    background: #1a1a1a;
    border-radius: 3px;
    overflow: hidden;
    display: none;
  }

  #vuBar {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #00ff88, #ffcc00, #ff4444);
    border-radius: 3px;
    transition: width 0.05s;
  }

  #photoStrip {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    max-width: 480px;
    margin-top: 16px;
  }

  #photoStrip img {
    width: 100px;
    height: 75px;
    object-fit: cover;
    border: 1px solid #222;
    border-radius: 2px;
    cursor: pointer;
  }

  canvas { display: none; }

  .cam-toggle {
    width: 100%;
    max-width: 480px;
    margin-top: 8px;
  }
</style>
</head>
<body>

<h1>&#9679; Camera &amp; Mic</h1>
<p class="subtitle">python · flask · webrtc</p>

<div id="videoContainer">
  <video id="video" autoplay playsinline muted></video>
  <div id="overlay"><p>[ stream inactive ]</p></div>
</div>

<div class="controls">
  <button id="btnStart" onclick="startStream()">▶ Start Stream</button>
  <button id="btnPhoto" onclick="takePhoto()" disabled>⬡ Capture</button>
  <button id="btnMic"   onclick="toggleMic()" disabled>⬡ Mic Monitor</button>
  <button id="btnStop"  onclick="stopStream()" disabled>■ Stop</button>
</div>

<button class="cam-toggle" id="btnFlip" onclick="flipCamera()" disabled style="max-width:480px;margin-top:8px;">
  ⇄ Flip Camera
</button>

<div id="vuMeter"><div id="vuBar"></div></div>
<div id="status">press start to request permissions</div>

<canvas id="canvas"></canvas>
<div id="photoStrip"></div>

<script>
let stream = null;
let audioCtx = null;
let analyser = null;
let vuRaf = null;
let micActive = false;
let facingMode = 'user'; // 'user' = front, 'environment' = back

const video   = document.getElementById('video');
const overlay = document.getElementById('overlay');
const vuMeter = document.getElementById('vuMeter');
const vuBar   = document.getElementById('vuBar');
const status  = document.getElementById('status');
const canvas  = document.getElementById('canvas');
const strip   = document.getElementById('photoStrip');

function setStatus(msg) { status.textContent = msg; }

async function startStream() {
  try {
    setStatus('requesting permissions…');
    stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode, width: { ideal: 1280 }, height: { ideal: 960 } },
      audio: true
    });
    video.srcObject = stream;
    overlay.classList.add('hidden');
    document.getElementById('btnStart').disabled = true;
    document.getElementById('btnPhoto').disabled = false;
    document.getElementById('btnMic').disabled   = false;
    document.getElementById('btnStop').disabled  = false;
    document.getElementById('btnFlip').disabled  = false;
    setStatus('streaming — camera + mic active');
  } catch (e) {
    setStatus('error: ' + e.message);
    console.error(e);
  }
}

function stopStream() {
  if (stream) stream.getTracks().forEach(t => t.stop());
  stream = null;
  video.srcObject = null;
  overlay.classList.remove('hidden');
  stopMicMonitor();
  document.getElementById('btnStart').disabled = false;
  document.getElementById('btnPhoto').disabled = true;
  document.getElementById('btnMic').disabled   = true;
  document.getElementById('btnStop').disabled  = true;
  document.getElementById('btnFlip').disabled  = true;
  setStatus('stream stopped');
}

function takePhoto() {
  if (!stream) return;
  const w = video.videoWidth, h = video.videoHeight;
  canvas.width = w; canvas.height = h;
  const ctx = canvas.getContext('2d');
  ctx.save();
  ctx.scale(-1, 1); ctx.drawImage(video, -w, 0, w, h); // un-mirror
  ctx.restore();
  const dataUrl = canvas.toDataURL('image/jpeg', 0.92);
  const img = document.createElement('img');
  img.src = dataUrl;
  img.title = 'Click to download';
  img.onclick = () => {
    const a = document.createElement('a');
    a.href = dataUrl;
    a.download = 'capture_' + Date.now() + '.jpg';
    a.click();
  };
  strip.prepend(img);
  setStatus('photo captured — click thumbnail to download');
}

function toggleMic() {
  micActive ? stopMicMonitor() : startMicMonitor();
}

function startMicMonitor() {
  if (!stream) return;
  audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  const source = audioCtx.createMediaStreamSource(stream);
  analyser = audioCtx.createAnalyser();
  analyser.fftSize = 256;
  source.connect(analyser);
  vuMeter.style.display = 'block';
  micActive = true;
  document.getElementById('btnMic').classList.add('active');
  document.getElementById('btnMic').textContent = '⬡ Mic ON';
  drawVU();
  setStatus('microphone monitor active');
}

function stopMicMonitor() {
  if (vuRaf) cancelAnimationFrame(vuRaf);
  if (audioCtx) audioCtx.close();
  vuMeter.style.display = 'none';
  vuBar.style.width = '0%';
  micActive = false;
  const btn = document.getElementById('btnMic');
  btn.classList.remove('active');
  btn.textContent = '⬡ Mic Monitor';
}

function drawVU() {
  const data = new Uint8Array(analyser.frequencyBinCount);
  analyser.getByteFrequencyData(data);
  const avg = data.reduce((a, b) => a + b, 0) / data.length;
  vuBar.style.width = Math.min(100, avg * 2.5) + '%';
  vuRaf = requestAnimationFrame(drawVU);
}

async function flipCamera() {
  facingMode = facingMode === 'user' ? 'environment' : 'user';
  if (stream) { stream.getTracks().forEach(t => t.stop()); }
  await startStream();
  // re-disable btnStart after flip
  document.getElementById('btnStart').disabled = true;
}
</script>
</body>
</html>
"""

def get_local_ip():
    """Get the machine's local network IP address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    ip = get_local_ip()
    print("\n" + "="*50)
    print("  Mobile Camera & Mic Access")
    print("="*50)
    print(f"\n  Local:   https://127.0.0.1:5000")
    print(f"  Network: https://{ip}:5000  ← open this on your phone")
    print("\n  Both devices must be on the same WiFi network.")
    print("  Note: Your browser may show a 'Not Secure' warning. You can safely bypass it.\n")
    app.run(host="0.0.0.0", port=5000, debug=False, ssl_context='adhoc')
