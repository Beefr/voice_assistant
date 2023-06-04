# voice_assistant  
Ceci est un voice assistant utilisant chatgpt avec de la reconnaissance vocale et visuelle.  
Les réponses apportées le sont vocalement.  
Il y a également une fonction de lecture de musique.  
Pas besoin de l'interpeller, elle réagit à la parole, mais pensez à lui dire de se taire ou sinon elle réagira à tout.  
  
Pour l'utiliser, pensez à vous générer une api-key sur openai et à la mettre dans un fichier key.txt à la racine du projet (à côté du main).  
  
Avant de commencer à essayer d'intéragir avec Sarah, attendez qu'elle vous dise bonjour.  
  
Les commandes:  
Vous pouvez lui dire:  
- "tais-toi" pour qu'elle s'arrête.  
- "Sarah" pour qu'elle se rallume.  
- Pour qu'elle regarde ce qui se passe via la caméra, dîtes le mot "regarde" puis posez votre question  
- Pour intéragir avec le lecteur de musiques, dîtes "lecteur musique", puis la commande:  
- next  
- previous  
- pause  
- relance  
- stop  
- play  
- ou sinon posez une question sur les musiques que vous avez  
  
- et enfin vous pouvez simplement poser n'importe quelle question  
  

Pour la musique, créez un dossier "library" dans le dossier musique, puis ajoutez vos musiques dans des dossiers dont le nom est le nom du groupe, ex: pour ajouter indochine - j'ai demandé à la lune, il faut un dossier indochine, puis mettre la musique dedans, on aurait donc: ...path.../voice_assistant/musique/library/indochine/jai_demande_à_la_lune.mp3  