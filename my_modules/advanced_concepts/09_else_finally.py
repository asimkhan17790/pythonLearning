try:
    a = 3545/0
except Exception as e:
    print("ERROR OCCURRED")
# Gets executed when there is no error in the try block
else:
    print("ALL Good. No error Was executed in the try block")
finally:
    print("Finally is Executed no matter what...")
