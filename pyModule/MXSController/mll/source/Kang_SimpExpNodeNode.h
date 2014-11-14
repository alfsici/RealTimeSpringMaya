#ifndef _Kang_SimpExpNodeNode
#define _Kang_SimpExpNodeNode
//
// Copyright (C) Kang
// 
// File: Kang_SimpExpNodeNode.h
//
// Dependency Graph Node: Kang_SimpExpNode
//
// Author: Maya Plug-in Wizard 2.0
//
#include <maya/MDagPathArray.h>
#include <maya/MPxCommand.h>
#include <maya/MArgList.h>
#include <maya/MPxNode.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnDagNode.h>
#include <maya/MItDependencyGraph.h>
#include <maya/MItDependencyNodes.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnGenericAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MTypeId.h> 
#include <maya/MFnNumericData.h>
#include <maya/MFnStringData.h>
#include <maya/MPlug.h>
#include <maya/MPlugArray.h>
#include <maya/MString.h>
#include <maya/MStringArray.h>
#include <maya/MDagPath.h>
#include <maya/MFloatVector.h>
#include "DynArray.h"
#include <string>
#include <algorithm>

class Kang_SimpExpNode : public MPxNode
{
public:
						Kang_SimpExpNode();
	virtual				~Kang_SimpExpNode(); 

	virtual MStatus		compute( const MPlug& plug, MDataBlock& data );

	static  void*		creator();
	static  MStatus		initialize();

public:
	bool	bPyImpExecuted;

	static  MObject		pyCmd;
	static  MObject		pyImportCmd;	
	static  MObject		inAttrNameArr;
	static  MObject		outAttrNameArr;


	// The typeid is a unique 32bit indentifier that describes this node.
	// It is used to save and retrieve nodes of this type from the binary
	// file format.  If it is not unique, it will cause file IO problems.
	//
	static	MTypeId		id;

	virtual MStatus         setDependentsDirty( const MPlug& plugBeingDirtied,
                                                                MPlugArray &affectedPlugs );

	//TArray<NotifiedInfo*> m_RefTargets; // �i�H�����h��Attr�ؼЦP�ɳQ�h�ӧ�s

	MStringArray m_InputAttrNames;
	MStringArray m_OutputAttrNames;

	//MStringArray m_pyCommandStrArr; // �Y�ɳB�z��Python Command�A�H \n �����}(str�����a \n)
	MString	m_pyCommandStr; 
	MString m_py_ImportCmdStr; // import ���������O�u��import�@���A�@���]�L�|�a��

	// 
	// MEL Command Functions
	//
	MStatus addNewInOutPair(MString inAttrName, MString outAttrName);
	// ���� �Y�� inOut ���p
	MStatus removeInOutPair(MString inAttrName, MString outAttrName);
};

class pyScriptNodeCmd_setPyCommandStr : public MPxCommand
{
public:
	MStatus doIt( const MArgList& args );
	static void* creator();
};

class pyScriptNodeCmd_setPyImportCommandStr : public MPxCommand
{
public:
	MStatus doIt( const MArgList& args );
	static void* creator();
};

class pyScriptNodeCmd_addNewInOutPair : public MPxCommand
{
public:
	MStatus doIt( const MArgList& args );
	static void* creator();
};

class pyScriptNodeCmd_removeInOutPair : public MPxCommand
{
public:
	MStatus doIt( const MArgList& args );
	static void* creator();
};

#endif
