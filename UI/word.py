import os

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn


class Doc:
    def __init__(self,file_name=None):
        if os.path.exists(file_name):
            self.file_name = file_name
            self.document=Document(file_name)
        else:
            self.file_name='python_code.docx'
            self.document=Document()

    def ClearText(self):
        # doc=Document()
        # doc.save(self.file_name)
        pass

    #添加标题
    def AddHeadText(self,text, size):
        title_ = self.document.add_heading(level=3)
        title_.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER# 标题居中
        title_run = title_.add_run(text)  # 添加标题内容
        title_run.font.size = Pt(size)  # 设置标题字体大小
        title_run.font.name = 'Times New Roman'  # 设置标题西文字体
        title_run.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')  # 设置标题中文字体
        title_run.font.color.rgb = RGBColor(0, 0, 0)#字体颜色

    #添加段落内容(参数1：文本内容，参数2：字体大小，参数3：上行距,参数4：字体粗细，参数5：段落位置)
    def AddParaText(self,text, size, space, thickness, position,front_name):
        p = self.document.add_paragraph()  # 段落
        p.paragraph_format.line_spacing = Pt(18)  # 18 磅
        #判断居中还是靠左,0为靠左
        if position == 0:
            p.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT #靠左
        else :
            p.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER #居中
        p.paragraph_format.space_before = Pt(space)
        text = p.add_run(text)
        #判断字体是否加粗（1为不加粗）
        if thickness == 1:
            text.bold = False
        else:
            text.bold = True #加粗
        text.font.name = 'Times New Roman'
        text.element.rPr.rFonts.set(qn('w:eastAsia'), front_name)
        text.font.size = Pt(size)
        self.document.save(self.file_name)
        return p

    def AddRunText(self,p,text,bond=False):
        r=p.add_run(text)
        r.font.name='Times New Roman'
        r.font.size = Pt(12)
        r.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
        self.document.save(self.file_name)

if __name__=='__main__':
    file_name='python_word.docx'
    doc=Doc(file_name)

    doc.AddParaText('标题',22,18,0,1,'隶书')#1为不加粗
    # zy=doc.AddParaText('摘 要：',12,18,0,0,'宋体')
    # doc.AddRunText(zy,'摘要里的内容')
    # kw=doc.AddParaText('关键字：',12,18,0,0,'宋体')
    # doc.AddRunText(kw,'关键字里面的内容')
    #
    #
    # yi=doc.AddParaText('一级标题\n',16,18,0,0,'宋体')
    # doc.AddRunText(yi,'正文'*30)
    #
    #
    # doc.AddParaText('参考文献',10.5,18,0,0,'宋体')
    # doc.ClearText()
