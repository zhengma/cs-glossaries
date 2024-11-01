"""
把一个文件夹里的 MarkDown 文件批量化转化为 PDF,
并保存在该文件所在文件夹下的 pdf 子文件夹里.

作者: 马正
组织: 渊学通教育广州分校, 上海科桥教育
创建日期: Oct. 2, 2024
最后修改日期: Oct. 2, 2024
Python版本: 3.12
"""

import os
import sys
import pypandoc

if __name__ == "__main__":
    pdoc_args = ['--metadata-file=layout.yaml', '--pdf-engine=xelatex']
    folder = sys.argv[1]
    if not os.path.exists(folder):
        print(f'{sys.argv[1]} does NOT exist!')
        exit()
    for root, dirs, files in os.walk(folder, topdown=True):
        for file in files:
            if file[-3:] == '.md':
                source = f'{root}/{file}'
                outf = f'{root}/pdf/{file[:-3]}.pdf'
                if (os.path.exists(outf) and
                    os.path.getmtime(outf) > os.path.getmtime(source)):
                    print(f'{source} has not changed since the last conversion.')
                    continue
                if not os.path.exists(f'{root}/pdf'):
                    os.mkdir(f'{root}/pdf')
                pypandoc.convert_file(source, 'pdf', outputfile=outf,
                                      extra_args=pdoc_args)
