# -*- coding: utf-8 -*-
# Last Modified 2013/11/21
# Author Chih Lun Kang
#�b���椧�e�A�� copy Python.Runtime.dll clr.pyd �o����ɮר� script Folder
import sys,os
import __builtin__
import shutil
import maya.mel
import maya.cmds as cmds

def listdir_joined(path):
	return [os.path.join(path, entry) for entry in os.listdir(path)]
	
def getfileRecursive(path,outArr):
	if(os.path.isfile(path)):
		_type_ = (path.split("."))[-1]
		#if(fileType == _type_):
		outArr.append(path)
	elif(os.path.isdir(path)):
		_folders_ = [x for x in listdir_joined(path)]
		for f in _folders_ :
			getfileRecursive(f,outArr)

class ClrDllCopier:
	# �غc�l�ѼƸѻ��G
	# nextClass : copy �һ�dll ���ᱵ�ۭn�إߪ�class
	# CurScrptPth : ��escript ������|
	def __init__(self,CurScrptPth=''):  #CurScrptPth='C:/PipeToolSet/VCAT/pyModule'
		self.thisScrptPth = CurScrptPth
		#self.__nextClassType__ = nextClass
		self.copyReqFileToFolder()
	def copyReqFileToFolder(self):
		#�P�_�����A�@�߰��]64bit
		mversion = str(maya.mel.eval("float $mayaVersion = `getApplicationVersionAsFloat` ;"))
		strMversion= mversion.split('.')[0]
		#script folder
		cpyDestFolder = str(maya.mel.eval("string $mayascrptfp = `internalVar -usd `"))
		plgFod = self.thisScrptPth + '/DotNet/clr/maya'+strMversion +'/'
		
		plgDllFile = plgFod+'Python.Runtime.dll'
		plgPydFile = plgFod+'clr.pyd'
		cpyDestDllFile=cpyDestFolder+'Python.Runtime.dll'
		cpyDestPydFile=cpyDestFolder+'clr.pyd'
		# ���i��|�������Ĭ�A���R��
		
		try:
			os.remove(cpyDestDllFile)
			os.remove(cpyDestPydFile)
		except:
			pass
		
		
		opRes=None
		if(os.path.isfile(cpyDestDllFile)):
			try:opRes = open(cpyDestDllFile,'r')
			except:pass
		#print("###############  OpenRes = "+ type(opRes).__name__ + "###########")
		if(not opRes): #�ɦs�b���ܴN����co�F
			try:res=os.makedirs(cpyDestFolder)#�j���Folder
			except:pass
			#Copy �һݪ�pyd files	
			#import shutil
			shutil.copy2(plgDllFile, cpyDestDllFile)
			shutil.copy2(plgPydFile, cpyDestPydFile)
		else:
			opRes.close()
		
		
		# �ƻs�һݪ��B�~�X�R�Ҳ� dll�G
		plgFodCustC = self.thisScrptPth + '/DotNet/clr/CustCtrls/'
		allDlls=[]
		getfileRecursive(plgFodCustC,allDlls)
		for d in allDlls:
			_file_ = d.split('/')[-1]
			_cpyDestFolder = cpyDestFolder+"CustCtrls/"
			_cpyDestDll = _cpyDestFolder + _file_
			# ���ն}��
			opRes=None
			if(os.path.isfile(_cpyDestDll)):
				try:opRes = open(_cpyDestDll,'r')
				except:pass
			if(not opRes): #�ɦs�b���ܴN����co�F
				try:res=os.makedirs(_cpyDestFolder)#�j���Folder
				except:pass
				#Copy �һݪ��B�~�X�R�Ҳ� dll	
				shutil.copy2(d,_cpyDestDll)
			else:
				opRes.close()
			
		#�[�J sys.path
		if(not cpyDestFolder in sys.path):
			sys.path.append(cpyDestFolder)
		# �[�J __builtin__ path
		__builtin__.DotNetDllPath = cpyDestFolder+"CustCtrls/"


