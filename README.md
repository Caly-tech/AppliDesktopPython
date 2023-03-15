usage : git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

Ci-dessous les commandes Git habituelles dans diverses situations :

démarrer une zone de travail (voir aussi : git help tutorial)
   clone     Cloner un dépôt dans un nouveau répertoire
   init      Créer un dépôt Git vide ou réinitialiser un existant

travailler sur la modification actuelle (voir aussi : git help revisions)
   add       Ajouter le contenu de fichiers dans l'index
   mv        Déplacer ou renommer un fichier, un répertoire, ou un lien symbolique
   restore   Restaurer les fichiers l'arbre de travail
   rm        Supprimer des fichiers de la copie de travail et de l'index

examiner l'historique et l'état (voir aussi : git help revisions)
   bisect    Trouver par recherche binaire la modification qui a introduit un bogue
   diff      Afficher les changements entre les validations, entre validation et copie de travail, etc
   grep      Afficher les lignes correspondant à un motif
   log       Afficher l'historique des validations
   show      Afficher différents types d'objets
   status    Afficher l'état de la copie de travail

agrandir, marquer et modifier votre historique
   branch    Lister, créer ou supprimer des branches
   commit    Enregistrer les modifications dans le dépôt
   merge     Fusionner deux ou plusieurs historiques de développement ensemble
   rebase    Réapplication des commits sur le sommet de l'autre base
   reset     Réinitialiser la HEAD courante à l'état spécifié
   switch    Basculer de branche
   tag       Créer, lister, supprimer ou vérifier un objet d'étiquette signé avec GPG

collaborer (voir aussi : git help workflows)
   fetch     Télécharger les objets et références depuis un autre dépôt
   pull      Rapatrier et intégrer un autre dépôt ou une branche locale
   push      Mettre à jour les références distantes ainsi que les objets associés

'git help -a' et 'git help -g' listent les sous-commandes disponibles et
quelques concepts. Voir 'git help <commande>' ou 'git help <concept>'
pour en lire plus à propos d'une commande spécifique ou d'un concept.
Voir 'git help git' pour un survol du système.
