#ifndef GRAPH_H
#define GRAPH_H
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define ROW 106
#define MAX 10
double longitude[ROW];
double latitude[ROW];

typedef struct coordinate
{
	double longitude;
	double latitude;
}Coordinate;
typedef double Side;
typedef struct graph
{
	Coordinate coordinate[ROW];
	Side side[ROW][ROW];
}Graph;
Graph graph;
void create(Graph*graph)
{
	FILE*file = NULL;
	char c = 0;
	char*str = (char*)malloc(sizeof(char));
	int a = 0;
	char*strArray[ROW][3];//strArray[行][列]
	char*strLine[ROW];
	char*temp = 0;
	char*nextTemp = 0;
	char*tempInLine = 0;
	char*nextTempInLine = 0;
	int row = 0;
	int column = 0;

	str[a] = 0;
	fopen_s(&file, "海南省所有镇的经纬度.txt", "r");
	c = (char)(fgetc(file));
	while (c != EOF)
	{
		str = (char*)realloc(str, (a + 2) * sizeof(char));//realloc(原指针,改变后的大小)
		str[a] = c;
		str[a + 1] = 0;
		c = (char)(fgetc(file));
		a++;
	}

	temp = strtok_s(str, "\n", &nextTemp);
	while (temp != NULL)
	{
		strLine[row] = temp;
		row++;
		temp = strtok_s(NULL, "\n", &nextTemp);
	}
	for (row = 0; row < ROW; row++)
	{
		tempInLine = strtok_s(strLine[row], ",", &nextTempInLine);
		while (tempInLine != NULL)
		{
			strArray[row][column] = tempInLine;
			column++;
			tempInLine = strtok_s(NULL, ",", &nextTempInLine);
		}
		column = 0;
	}

	for (row = 0; row < ROW; row++)
	{
		longitude[row] = atof(strArray[row][1]);
		latitude[row] = atof(strArray[row][2]);
	}

	fclose(file);
	free(str);
	str = NULL;
	file = NULL;

	for (row = 0; row < ROW; row++)
	{
		graph->coordinate[row].longitude = longitude[row];
		graph->coordinate[row].latitude = latitude[row];
	}
	for (row = 0; row < ROW; row++)
	{
		for (column = 0; column < ROW; column++)
		{
			graph->side[row][column] = MAX;
		}
	}
}
#endif