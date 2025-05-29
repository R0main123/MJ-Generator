import os
for file in os.listdir("data/"):
    if file.endswith(".txt"):
        in_filename =  os.path.join("data/", file)
        out_filename_verse = os.path.join("data/Verse", file)
        out_filename_chorus = os.path.join("data/chorus", file)
        with open(in_filename, "r", encoding="utf-8") as infile, open(out_filename_verse, "w", encoding="utf-8") as outfile_verse, open(out_filename_chorus, "w", encoding="utf-8") as outfile_chorus:
            paragraph = []
            for line in infile:
                if line.strip() == "":
                    # Fin d'un paragraphe
                    if paragraph and paragraph[0].startswith("[Verse"):
                        outfile_verse.writelines(paragraph[1:])
                        outfile_verse.write("\n")
                    elif paragraph and paragraph[0].startswith("[Chorus"):
                        outfile_chorus.writelines(paragraph[1:])
                        outfile_chorus.write("\n")
                    paragraph = []  # Réinitialiser le paragraphe
                else:
                    paragraph.append(line)

            # Vérifie le dernier paragraphe (s'il n'est pas suivi par une ligne vide)
            if paragraph and paragraph[0].startswith("[Verse"):
                outfile_verse.writelines(paragraph[1:])
            elif paragraph and paragraph[0].startswith("[Chorus"):
                outfile_chorus.writelines(paragraph[1:])
