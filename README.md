# commons-util-py
Common util functions for Python


# Usage
Note to rename the root folder to `util`  
```bash
git clone git@github.com:idf/commons-util-py.git util
```

Use as subtree  
```bash
git remote add -f util git@github.com:idf/commons-util-py.git
git subtree add --prefix util util develop --squash
git subtree pull --prefix util util develop --squash
git subtree push --prefix util util develop 
```

# Interface
Compile-time enforcement of interface specifications helps in the construction of large programs. In Python you have to 
write more tests. An appropriate testing discipline can help build large complex applications in Python as well as 
having interface specifications would. [ref: Python Design](https://docs.python.org/2/faq/design.html)