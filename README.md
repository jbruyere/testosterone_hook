# testosterone_hook

Pour tester l'utilisation du hook
---------------------------------

- Copier les fichiers contenu de le fichier ./hook dans .git/hook
    `pre-commit` s'execute automatiquement AVANT un `git commit`
    `commit̀` s'execute automatiquement APRES un `git commit`
- Modifier un fichier, puis l'`add` et le `commit`
- Se rendre compte de se qu'il se passe lors du Commit


Pour tester soit même des scripts
---------------------------------

- avoir un script (Python, Bash ou autre...) dans le dossier .git/hook
- son nom définit le moment où le script va être éxecuté
- Les noms possibles: `applypath-msg`, `commit-msg`, `fsmonitor-watchman`, `post-update`, `pre-applypatch`, `pre-commit`, `pre-push`, `pre-rebase`, `pre-receive`, `prepare-commit-message`, `update`

Pour plus d'infos
-----------------
https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks
https://www.atlassian.com/git/tutorials/git-hooks
https://docs.python.org/fr/3/library/unittest.html
    