#include"Graph.h"
#include"GA.h"
#include"Python.h"
int getRow()
{
	return ROW;
}
int longitudeMin()
{
	double min = longitude[0];
	int i = 1;
	for (i = 1; i < ROW; i++)
	{
		if (longitude[i] < min)
		{
			min = longitude[i];
		}
	}
	return (int)min;
}
int latitudeMin()
{
	double min = latitude[0];
	int i = 1;
	for (i = 1; i < ROW; i++)
	{
		if (latitude[i] < min)
		{
			min = latitude[i];
		}
	}
	return (int)min;
}
static PyObject* core_getRow(PyObject *self, PyObject *args)
{
	return (PyObject*)Py_BuildValue("i", getRow());
}
static PyObject* core_initGraph(PyObject *self, PyObject *args)
{
	create(&graph);
	minGraph(&graph);
	return (PyObject*)Py_BuildValue("");
}
static PyObject* core_getPoint(PyObject *self, PyObject *args)	//�⣺core��������getPoint
{
	int x;
	int y;
	int i;
	if (!PyArg_ParseTuple(args, "i", &i))	//"i":int
	{
		return NULL;
	}
	return (PyObject*)Py_BuildValue("iii", i, x = (int)((longitude[i] - longitudeMin()) * 300), y = (int)((latitude[i] - latitudeMin()) * 300));
}
static PyObject* core_getSide(PyObject *self, PyObject *args)
{
	int i;
	int j;
	if (!PyArg_ParseTuple(args, "ii", &i,&j))	//"i":int
	{
		return NULL;
	}
	if (graph.side[i][j] < 10)
	{
		return (PyObject*)Py_BuildValue("i", 1);
	}
	return (PyObject*)Py_BuildValue("i", 0);
}
static PyMethodDef coreMethods[] =	//�⣺core�������б�
{
	{"getPoint",core_getPoint,METH_VARARGS,"" },
	{"getRow",core_getRow,METH_VARARGS,""},
	{"getSide",core_getSide,METH_VARARGS,"" },
	{"initGraph",core_initGraph,METH_VARARGS,"" },
	{ NULL, NULL, 0, NULL },	//PyModuleDef_HEAD_INIT
};
static struct PyModuleDef coreMoudle =	//�⣺core
{
	PyModuleDef_HEAD_INIT,
	"core",
	NULL,
	-1,
	coreMethods
};
void PyInit_core()	//�⣺core
{
	PyModule_Create(&coreMoudle);
}