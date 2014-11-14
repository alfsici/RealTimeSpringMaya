# -*- coding: utf-8 -*-
# Last Modified 2013/11/25
# Author Chih Lun Kang
import os
import __builtin__
try:import clr
except:pass
if(clr):
		#clr.AddReference("System")
		#clr.AddReference("System.IO")
		#clr.AddReference("System.Windows")

		import System
		import System.IO
		import System.Reflection
		import System.Windows.Forms
		
		asm = System.Reflection.Assembly
		asm = asm.LoadWithPartialName("PresentationFramework") # ���J�һݪ�dll
		import System.Windows
		Assembly = System.Reflection.Assembly
		# ���J�B�~���X�Rdll
		res=None
		try:
			if( __builtin__.DotNetDllPath):
				_sldGrpDllPth = __builtin__.DotNetDllPath+"SldGrp.dll"
				res = Assembly.LoadFrom ( _sldGrpDllPth )
		except:pass
		try:import SldGrp
		except:pass
		# https://code.google.com/p/phoenix-control-library/wiki/Usage
		# pcl.NumericSpinnerControl
		try:
			if( __builtin__.DotNetDllPath):
				_wpfSpinDllPth = __builtin__.DotNetDllPath+"WpfSpinnerCtrl.dll"
				res = Assembly.LoadFrom ( _wpfSpinDllPth )
		except:pass
		try:import PhoenixControlLib
		except:pass
		
		# ��wpf �i�H�O�J winform
		inte = asm.LoadWithPartialName("WindowsFormsIntegration")
		if(inte):
			import System.Windows.Forms.Integration

def createWinFromXaml(xamlAbsPth):
	if(clr):
		if( (xamlAbsPth)and(os.path.isfile(xamlAbsPth)) ):
			XamlReader= System.Windows.Markup.XamlReader()
			XamlString = System.IO.File.ReadAllText(xamlAbsPth)
			XamlCtrl=XamlReader.Parse(XamlString)
			return XamlCtrl


# ���^�X�W�Y�ӱ�����U�Ҧ�����������
def GetChildRecursive(parent,ourArr):
	treeHlp = System.Windows.LogicalTreeHelper
	children=treeHlp.GetChildren(parent)
	for e in children:
		if( issubclass( type(e) ,System.Windows.DependencyObject)):
			ourArr.append(e)
			GetChildRecursive(e, ourArr)

# ���^�M��Y�ӱ�����U�Y����������
def GetChildRecursiveByType(parent,_type_,ourArr):
	treeHlp = System.Windows.LogicalTreeHelper
	children=treeHlp.GetChildren(parent)
	for e in children:
		if( issubclass( type(e) ,System.Windows.DependencyObject)):
			if ( type(e) is _type_):
				ourArr.append(e)
			GetChildRecursiveByType(e,_type_, ourArr)

# �Ǧ^�Y�ӱ�����U�P�������M��
def GetChildListByType(parent,_type_):
	if(clr):
		import System.Windows
		arr = []
		GetChildRecursiveByType(parent,_type_,arr)
		return arr

# �̾ڦW�٧䱱��
def GetChildByName(parent,_name_=""):
	if(clr):
		arr = []
		GetChildRecursive(parent,arr)
		for c in arr:
			if(c.Name):
				if(c.Name == _name_):
					return c
					break

# �������ӱ��󩳤U�Ҧ��l����
def removeAllChildFromControl(parent): #parent = SkelPanel
	remList=[]
	for ch in parent.Children:
		remList.append(ch)
	for k in (len(remList)-1,0,-1):
		parent.Children.Remove(remList[k])


# �[�JSld Grp ����w Control�U
# Slider Group �O���Ʀr��J��Slider ���Q�|�椬�s��
def AddSldGrpToControl(parent):
	if(SldGrp):
		sldgrp = SldGrp.UserControl1()
		parent.Children.Add(sldgrp)

# ���ª�WinForm����[��wpf����U�A���A�]�@�h Integration
def AddWinFormCtrlToWpfCtrl(parent,child):
	intr=None
	try:intr = System.Windows.Forms.Integration
	except:pass
	if intr:
		host = System.Windows.Forms.Integration.WindowsFormsHost()
		host.Child = child
		parent.Children.Add(host)
'''

sldgrp = SldGrp.UserControl1()
sldGrpPanel.Children.Add(sldgrp)



allBtn = GetChildByType(__builtin__.g_Pipe12SkelTool,System.Windows.Controls.Button)
allStPanel = GetChildByType(__builtin__.g_Pipe12SkelTool,System.Windows.Controls.StackPanel) 
for b in allStPanel: # b = allStPanel[1]
	b.Background
	b.Name=="SkelCtrlPanel"
panel_ = GetChildByName(__builtin__.g_Pipe12SkelTool , _name_="SkelCtrlPanel")
'''