import sys
import argparse


def main():
    # sys.argv is a simpler way to retrieve command line arguments. Use it when you expect simple command line inputs. 
    args = sys.argv[1:]
    print(sys.argv[2])
    print(args)
    a = input('Enter something')
    print(a)

# def main():
#     # argparse module is used to retrieve command line arguments that are more complex. 
#     parser = argparse.ArgumentParser(description='Process some integers.') # create an instance of argparse 
#     parser.add_argument('--mode', type=str, required=True) # call the add_argument method to accept a new argument 
#     args = parser.parse_args()
#     print (args.mode)


# def main():
#     while True:
#         reply = input('Enter text:')
#         if reply == 'stop': break
#         try:
#             num = int(reply)
#         except:
#             print('Bad' * 8)
#         else:
#             print(num ** 2)
#     print('Bye')

if __name__=="__main__":
    main()