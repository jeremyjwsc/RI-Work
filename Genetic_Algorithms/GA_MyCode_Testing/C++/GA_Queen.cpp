
/*****************************************************************************/ 
//  Genetic Algorithms
//  RI (C++ Code Report)
//  November, 2018
//  by JW
/*****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

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
	int CostMatrix[1000];// to keep cost value for each chromosome
	int CrossOverMatrix[30][1000];// to keep cross over matrix for relative parents
	int Population;
	int Iteration;
	float MutationRate ;
	int ChessBoradLenght;
	

private:
	int area[30][30];// This is the chess board matrix
	


};


//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

CGAQueen::CGAQueen(int nPopulation,int nIteration,float Mutation,int iChBoard)
{
	Clear();
	srand( (unsigned)time( NULL ) );
	Population=nPopulation;
	Iteration=nIteration;
	MutationRate=Mutation;
	ChessBoradLenght=iChBoard;
	
}

CGAQueen::~CGAQueen()
{

}

int CGAQueen::CostFunc(int index)
{
	// Determine The CostFunction of matrix[][index] and return the Cost Value
	// The Best Cost is zero 
	int costValue=0;
	int m,n;
	int i,j;
			
	for(i=0;i<ChessBoradLenght;i++)
	{	
		j=ChromosomeMatrix[i][index];

		m=i+1;
		n=j-1;
		while(m<ChessBoradLenght	&& n>=0)
		{
			if(area[m][n]==1)
			{
				costValue++; // there is a queen that takes the other one 
			}
			m++;
			n--;
		}

		m=i+1;
		n=j+1;
		while(m<ChessBoradLenght && n<ChessBoradLenght )
		{		
			if(area[m][n]==1)
			{
				
				costValue++;// there is a queen that takes the other one 
			}
			m++;
			n++;
		}

		m=i-1;
		n=j-1;
		while(m>=0 && n>=0)
		{		
			if(area[m][n]==1)
			{
				
				costValue++;// there is a queen that takes the other one 
			}
			m--;
			n--;
		}
		
		m=i-1;
		n=j+1;
		while(m>=0 && n<ChessBoradLenght)
		{		
			if(area[m][n]==1)
			{
				
				costValue++;// there is a queen that takes the other one 
			}
			m--;
			n++;
		}
	}

	return costValue;
	
}

void CGAQueen::Clear()
{
	// to Reset All cells 
	for (int i=0;i<ChessBoradLenght;i++)
		for (int j=0;j<ChessBoradLenght;j++)
			area[i][j]=0;
}

void CGAQueen::InitialPopulation() 
{
	
	int random;
	bool bCheck;
	for (int index=0;index<=Population-1;index++)
		for (int a=0;a<ChessBoradLenght;a++)
			{
				random=rand();
				
				bCheck=1;
				for (int b=0;b<a;b++)
					if (random%ChessBoradLenght==ChromosomeMatrix[b][index])
						bCheck=0;
				if (bCheck)
					ChromosomeMatrix[a][index]=random%ChessBoradLenght;
				else
					a--;
			}

}
void CGAQueen::PopulationSort()
{
	bool k=1;
	int Temp;
	while(k)
	{
		k=0;
		for (int i=0;i<=Population-2;i++)
		{
			if (CostMatrix[i]>CostMatrix[i+1])	
			{
				Temp=CostMatrix[i];
				CostMatrix[i]=CostMatrix[i+1];
				CostMatrix[i+1]=Temp;
				
			for (int j=0;j<ChessBoradLenght;j++)
			{
				Temp=ChromosomeMatrix[j][i];
				ChromosomeMatrix[j][i]=ChromosomeMatrix[j][i+1];
				ChromosomeMatrix[j][i+1]=Temp;
			}			
			k=1;
			}
		}
	}
}
void CGAQueen::Mating()
{
	int TempMatrix[30][2];
	int TempMatrix0[30],TempMatrix1[30];
	int Temp,i, j,k;

	for (int index=0;index<=(Population/4)-1;index++)
		for (int t=0;t<=1;t++)
		{
			
			for(i=0;i<ChessBoradLenght;i++)
			{
				TempMatrix0[i]=ChromosomeMatrix[i][2*index];
				TempMatrix1[i]=ChromosomeMatrix[i][2*index+1];
			}
			for (i=0;i<ChessBoradLenght;i++)
				if(CrossOverMatrix[i][2*index+t]==0)
				{
					for (j=0;j<ChessBoradLenght;j++)
						if(TempMatrix0[j]!=100)	
						{
							TempMatrix[i][t]=TempMatrix0[j];
							Temp=TempMatrix0[j];
							TempMatrix0[j]=100;
							j=ChessBoradLenght-1;
						
							for (k=0;k<ChessBoradLenght;k++)
							{
								if (TempMatrix1[k]==Temp)
								{
									TempMatrix1[k]=100;
									k=ChessBoradLenght-1;
								}
							}
						}
				}
				else
				{
					for (j=0;j<ChessBoradLenght;j++)
						if(TempMatrix1[j]!=100)	
						{
							TempMatrix[i][t]=TempMatrix1[j];
							Temp=TempMatrix1[j];
							TempMatrix1[j]=100;
							j=ChessBoradLenght-1;
						
							for (k=0;k<ChessBoradLenght;k++)
							{
								if (TempMatrix0[k]==Temp)
								{
									TempMatrix0[k]=100;
									k=ChessBoradLenght-1;
								}
							}
						}
				}

		for(i=0;i<ChessBoradLenght;i++)
			ChromosomeMatrix[i][2*index+Population/2+t]=TempMatrix[i][t];
		
		}

	
}
void CGAQueen::GenerateCrossOverMatrix()
{
	// generate a matrix with random 0's and 1's
	int randomCrossOver;
	for (int index=0;index<=Population-1;index++)
		for (int a=0;a<ChessBoradLenght;a++)
		{
			randomCrossOver=rand();
			CrossOverMatrix[a][index]=randomCrossOver%2;
		}

}
void CGAQueen::ApplyMutation()
{
	// a random for selecting chromosome
	// a random for selecting genes from selected chromosome

	int randomChromosome;
	int randomGen0,randomGen1;
	int Temp;
	// the following formula is a mutation formula to obtain the number of Mutation
	int NumberOfMutation=int(MutationRate*(Population-1)*ChessBoradLenght);
	
	for(int k=0;k<=NumberOfMutation;k++)
	{
		randomChromosome=0;
		while((randomChromosome=rand()%Population)==0);// random chromosome exept number 0
			
		randomGen0=rand()%ChessBoradLenght;// random genes from chromosome
		while((randomGen1=rand()%ChessBoradLenght)==randomGen0);
		
		// Apply Mutation
		Temp=ChromosomeMatrix[randomGen0][randomChromosome];
		ChromosomeMatrix[randomGen0][randomChromosome]=ChromosomeMatrix[randomGen1][randomChromosome];
		ChromosomeMatrix[randomGen0][randomChromosome]=Temp;
	}
	
}
void CGAQueen::FillArea(int index)
{
	// to Fill Area with Desired Solution Matrix
	Clear();
	for (int i=0;i<ChessBoradLenght;i++)
		area[i][ChromosomeMatrix[i][index]]=1;

	// after this if there is a queen in a cell , its value will be 1
	// The other cells value will be 0


}

int main(int argc, char* argv[])
{
	int population;
	int iteration;
	float mutation_rate;
	int board = 8;			// this is only for 8 queen

	if(argc < 4){
		
		// use default values
		population = 100;
		iteration = 10;
		mutation_rate = 0.5;
		
		fprintf(stderr, "Usage and Running: %s\n", argv[0]);
		fprintf(stderr, "Default parameters:\n\t population=%d\n\t iteration=%d\n\t mutation_rate=%d\n\t board=%d\n", 
		                 population,iteration,mutation_rate,board);
		
	} else{
		population = atoi(argv[1]);
		iteration = atoi(argv[2]);
		mutation_rate = atof(argv[3]);
	}

	int i, k=0, g=0, num=0;
	char a = 'g';

	CGAQueen Sample(population, iteration, mutation_rate, board);

	Sample.InitialPopulation();

	while(g==0 && num<Sample.Iteration)
	{
		num++;
		g=0;

		for (k=0;k<=Sample.Population-1;k++)
		{
			Sample.FillArea(k);
			Sample.CostMatrix[k]=Sample.CostFunc(k);
		}

		Sample.PopulationSort();

		if (Sample.CostMatrix[0]==0)
			g=1;


		Sample.GenerateCrossOverMatrix();

		Sample.Mating();

		Sample.ApplyMutation();

	}


	char* result = (char*)malloc(256);
	char tmp[10];
	sprintf(result, "result:\n\t");

	for (i=0; i<board-1; i++)
	{
		sprintf(tmp, "%d_",Sample.ChromosomeMatrix[i][0]);
		strcat(result, tmp);
	}
	sprintf(tmp, "%d\n",Sample.ChromosomeMatrix[board-1][0]);
	strcat(result, tmp);

	fprintf(stdout, result);

	free(result);



	return 0;
}
