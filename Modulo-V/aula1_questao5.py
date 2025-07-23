import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:\n")

frase = input("Digite uma frase e ela será emojizada:\n")

frase_emojizada = emoji.emojize(frase, language='alias')

print("\nFrase emojizada:")
print(frase_emojizada)
