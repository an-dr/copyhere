# copyhere

A package to copy or unzip a file to cwd

Pypi: https://pypi.org/project/copyhere/

![how it works picture](https://www.lucidchart.com/publicSegments/view/19b528bf-a8e0-40ac-b868-64367f268646/image.png)

## install

pip install copyhere

## run

```bash
python -m copyhere
```

or

```python
import copyhere
copyhere.start()    # name=None (default) for using source file name
                    # name='' for user input a new name,
                    # name="any your new name"
```

to specify a folder to open in the selection window use `COPYHERE_SOURCEDIR` environment variable
