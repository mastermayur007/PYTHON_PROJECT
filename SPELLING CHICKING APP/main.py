from spellchecker import SpellChecker

class SpellCheckingApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        
        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}'")
            corrected_words.append(corrected_word)
                
        return ' '.join(corrected_words)
    
    def run(self):
        print("\n======= Spell Checker ==========")
        
        while True:
            text = input("Enter the text (type 'exit' to close): ")
            if text.lower() == "exit":
                print("Closing the program...")
                break
            corrected_text = self.correct_text(text)
            print(f"Corrected text: {corrected_text}")

if __name__ == "__main__":
    SpellCheckingApp().run()
