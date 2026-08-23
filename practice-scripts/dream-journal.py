print("📓 Welcome to Your Dream Journal")

date = input("enter a date of your dream: ")
words = input("enter your dream: ")
dreams = {
    date : words
}
print("--- Dream Saved! 🌙 ---")
print(date,":",dreams.get(date))
