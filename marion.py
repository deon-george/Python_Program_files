#marion
def main():
    a = int(input("Enter a value for 'a': ")) 
     # Ask for 'a' directly
    col(a)

def col(a):
    for _ in range(a): 
         # Use an underscore for the loop variable if it's not needed
        print("#" * a)


#if __name__ == "__main__":
main()




  
