source venv/bin/activate
./venv/bin/mkdocs build
 cd open-c3.github.io
 git reset 23caecfd2cb6e6db3e2716adf9118ac4ea8a562d
 git clean -fd
 rsync -av ../site/ ./
 git add .
 git commit -m u
 git push -f
 cd ..
 ./sync.sh
