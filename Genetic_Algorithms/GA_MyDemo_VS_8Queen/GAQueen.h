// GAQueen.h: interface for the CGAQueen class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_GAQUEEN_H__C26AE0A3_F9B4_426F_A324_B460CC7946CB__INCLUDED_)
#define AFX_GAQUEEN_H__C26AE0A3_F9B4_426F_A324_B460CC7946CB__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000


class CGAQueen  
{
public:
	CGAQueen(int nPopulation,int nIteration,float Mutation,int mChBoard);
	virtual ~CGAQueen();
	void Clear();// to clear chess board with 0 value
	void InitialPopulation();// to create the first and initial randompopulation
	void FillArea(int index);// to fill chess board with desired chromosome
	int CostFunc(int index);// determine the cost of matrix[index][index]
	void PopulationSort();// to sort population from the best to the worst
	void GenerateCrossOverMatrix();// a way to create children from parent is CcrossOver
	void Mating();// to create children from parents
	void ApplyMutation();// to apply mating to sorted population from the second chromosome to last

	int ChromosomeMatrix[30][1000];// Answer ( chromosome ) Matrix 
	int CostMatrix[1000];// to keep cost va;ue for each chromosome
	int CrossOverMatrix[30][1000];// to keep cross over matrix for relative parents
	int Population;
	int Iteration;
	float MutationRate ;
	int ChessBoradLenght;
	

private:
	int area[30][30];// This is the chess board matrix
	


};

#endif // !defined(AFX_GAQUEEN_H__C26AE0A3_F9B4_426F_A324_B460CC7946CB__INCLUDED_)
