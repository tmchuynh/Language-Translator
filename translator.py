from tkinter import *
from translate import Translator

Screen = Tk()
Screen.title("Language Translator")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

LanguageChoices = {'Japanese', 'English', 'French', 'Italian', 'Russian', 'Chinese', 'Latin', 'Greek', 'Hawaiian', 'German', 'Vietnamese', 'Spanish'}

InputLanguageChoice.set('English')
TranslateLanguageChoice.set('German')

def Translate():
    translator = Translator(
        from_lang = InputLanguageChoice.get(),
        to_lang = TranslateLanguageChoice.get()
    )
    # translates the text
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)


# Choice for the input languages
InputLanguageChoiceMenu = OptionMenu(
    Screen,
    InputLanguageChoice,
    *LanguageChoices
)
InputLanguageChoiceMenu.config(width = 8)

# Implements the display boxes
Label(
    Screen,
    text= "Choose a language"). grid(row = 0, column = 1)
# Widgets are arranged on the screen
InputLanguageChoiceMenu.grid(row = 1, column = 1)

# Choice for the output languages
NewLanguageChoiceMenu = OptionMenu(
    Screen,
    TranslateLanguageChoice,
    *LanguageChoices
)
NewLanguageChoiceMenu.config(width = 8)

Label(
    Screen,
    text="Translated Language").grid(row = 0, column = 2)
NewLanguageChoiceMenu.grid(row = 1, column = 2)

Label(
    Screen,
    text = "Enter text:"
).grid(row = 2, column = 0)
TextVar = StringVar()
TextBox = Entry(
    Screen,
    textvariable = TextVar).grid(row = 2, column = 1)

Label(
    Screen,
    text = "Output text"
).grid(row = 2, column = 2)
OutputVar = StringVar()
TextBox = Entry(
    Screen,
    textvariable = OutputVar).grid(row = 2, column = 3)

# Creates the translate button with a 3d effect
B = Button(
    Screen,
    text = "translate",
    command = Translate,
    relief = GROOVE).grid(row = 3, column = 1, columnspan = 3)

mainloop()