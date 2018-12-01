// ChessDlg.cpp : implementation file
//

#include "stdafx.h"
#include "Chess.h"
#include "ChessDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CChessDlg dialog

CChessDlg::CChessDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CChessDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CChessDlg)
	m_Iteration = 0;
	m_Population = 0;
	m_ChBoard = 0;
	m_BestAnswer = _T("");
	m_Generation = 0;
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CChessDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CChessDlg)
	DDX_Control(pDX, IDC_MyStatic, m_myStatic);
	DDX_Text(pDX, IDC_Iteration, m_Iteration);
	DDV_MinMaxInt(pDX, m_Iteration, 1, 5000);
	DDX_Text(pDX, IDC_Population, m_Population);
	DDV_MinMaxInt(pDX, m_Population, 1, 1000);
	DDX_Text(pDX, IDC_Mutation, m_MutationRate);
	DDV_MinMaxFloat(pDX, m_MutationRate, 0.f, 1.f);
	DDX_Text(pDX, IDC_ChessBoard, m_ChBoard);
	DDX_Check(pDX, IDC_GrAnimate, m_Animate);
	DDX_Check(pDX, IDC_Graphic, m_Graphic);
	DDX_Check(pDX, IDC_BestDisplay, m_BestDisplay);
	DDX_Text(pDX, IDC_BestAnswer, m_BestAnswer);
	DDX_Text(pDX, IDC_BestCost, m_BestCost);
	DDX_Text(pDX, IDC_Generation, m_Generation);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CChessDlg, CDialog)
	//{{AFX_MSG_MAP(CChessDlg)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_Start, OnStart)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CChessDlg message handlers

BOOL CChessDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	m_Iteration=10;
	m_Population=100;
	m_MutationRate=.5;
	m_ChBoard=8;

	m_BestDisplay = 1;

	UpdateData(0);
	return TRUE;  // return TRUE  unless you set the focus to a control
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CChessDlg::OnPaint() 
{
	
	
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	
	}
	else
	{
		CDialog::OnPaint();
	}

}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CChessDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CChessDlg::OnOK() 
{
	CDialog::OnOK();
	// TODO: Add extra validation here

}

void CChessDlg::PlaceQueen(int index,int row,int column)
{
	int x,y;
	
	CDC* mmm;
	mmm=m_myStatic.GetDC();
	
	
	COLORREF crColor=RGB(255,0,0);
	CPen pen1 (PS_SOLID, 2, crColor);
	mmm->SelectObject (&pen1);
	

	y=(303/index)*row+(160/index);
	x=(303/index)*column+(160/index);
	
	int r=(75/index);
	mmm->MoveTo(x+r,y);
	mmm->AngleArc(x,y,r,0,360);



}

void CChessDlg::InitializeBoard(int index)
{
	int tt,yy;
	CDC* mmm;
	mmm=m_myStatic.GetDC();

	
	mmm->SetMapMode (MM_ISOTROPIC);
    mmm->SetWindowExt (1000, 1000);
    mmm->SetViewportExt (1000, 1000);
    mmm->SetViewportOrg (0, 0);
	

	COLORREF crColor=RGB(0,255,0);
	CPen penGreen (PS_SOLID, 1, crColor);
	mmm->SelectObject (&penGreen);

	mmm->MoveTo(0,0);
	mmm->LineTo(0,300);
	mmm->LineTo(300,300);
	mmm->LineTo(300,0);
	mmm->LineTo(0,0);

	crColor=::GetSysColor(COLOR_3DFACE);
	CBrush brsSys(crColor);
	mmm->SelectObject(&brsSys);
	mmm->FloodFill(1,1,RGB(0,255,0));
	

	crColor=RGB(0,0,255);
	CPen penBlue (PS_SOLID, 1, crColor);
	mmm->SelectObject (&penBlue);
	
	
	for (int i=0;i<=index;i++)
	{
		
		mmm->MoveTo(3,(303/index)*i+3);
		mmm->LineTo(303,(303/index)*i+3);
		
		mmm->MoveTo((303/index)*i+3,3);
		mmm->LineTo((303/index)*i+3,303);
	}

	
	CBrush brsWhite(RGB(255,255,255));
	mmm->SelectObject(&brsWhite);

	for (int j=0;j<index;j+=2)
		for (int i=0;i<index;i+=2)
		{
			tt=(300/index)*i+(150/index);
			yy=(300/index)*j+(150/index);
			mmm->FloodFill(tt,yy,RGB(0,0,255));
		}

	for (int j=1;j<index;j+=2)
		for (int i=1;i<index;i+=2)
		{
			tt=(300/index)*i+(150/index);
			yy=(300/index)*j+(150/index);
			mmm->FloodFill(tt,yy,RGB(0,0,255));
		}

	CBrush brsBlack(RGB(0,0,0));
	mmm->SelectObject(&brsBlack);

	for (int j=1;j<index;j+=2)
		for (int i=0;i<index;i+=2)
		{
			tt=(300/index)*i+(150/index);
			yy=(300/index)*j+(150/index);
			mmm->FloodFill(tt,yy,RGB(0,0,255));
		}

	for (int j=0;j<index;j+=2)
		for (int i=1;i<index;i+=2)
		{
			tt=(300/index)*i+(150/index);
			yy=(300/index)*j+(150/index);
			mmm->FloodFill(tt,yy,RGB(0,0,255));
		}


	
}

void CChessDlg::ClearArea(int index)
{
	/////////////////////	
	
	int tt,yy,i,j;
	CDC* mmm;
	mmm=m_myStatic.GetDC();

	COLORREF  crColor=RGB(0,0,255);
	CPen penBlue (PS_SOLID, 1, crColor);
	mmm->SelectObject (&penBlue);
	
	
	for (i=0;i<=index;i++)
	{
		
		mmm->MoveTo(3,(303/index)*i+3);
		mmm->LineTo(303,(303/index)*i+3);
		
		mmm->MoveTo((303/index)*i+3,3);
		mmm->LineTo((303/index)*i+3,303);
	}
	
	CBrush brsWhite(RGB(255,255,255));
	mmm->SelectObject(&brsWhite);

	for (j=0;j<index;j+=2)
		for (i=0;i<index;i+=2)
		{
			if (FillMatrix[j]==i)
			{
				tt=(300/index)*i+(150/index);
				yy=(300/index)*j+(150/index);
				mmm->FloodFill(tt,yy,RGB(0,0,255));
			}
		}

	for (j=1;j<index;j+=2)
		for (i=1;i<index;i+=2)
		{
			if (FillMatrix[j]==i)
			{
				tt=(300/index)*i+(150/index);
				yy=(300/index)*j+(150/index);
				mmm->FloodFill(tt,yy,RGB(0,0,255));
			}
		}
	
	CBrush brsBlack(RGB(0,0,0));
	mmm->SelectObject(&brsBlack);

	for (j=1;j<index;j+=2)
		for (i=0;i<index;i+=2)
		{
			if (FillMatrix[j]==i)
			{
				tt=(300/index)*i+(150/index);
				yy=(300/index)*j+(150/index);
				mmm->FloodFill(tt,yy,RGB(0,0,255));
			}
		}

	for (j=0;j<index;j+=2)
		for (i=1;i<index;i+=2)
		{
			if (FillMatrix[j]==i)
			{
				tt=(300/index)*i+(150/index);
				yy=(300/index)*j+(150/index);
				mmm->FloodFill(tt,yy,RGB(0,0,255));
			}
		}
}

void CChessDlg::OnStart() 
{
	// TODO: Add your control notification handler code here
	UpdateData(1);
	
	
	int i,k=0,g=0,num=0;	
	char  a='g';
	
	if(m_ChBoard<=30)
	{
		CGAQueen Sample(m_Population,m_Iteration,m_MutationRate,m_ChBoard);
	
		if(m_Graphic)
			InitializeBoard(m_ChBoard);

		Sample.InitialPopulation();

		CString as,gs;
		

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
					
			
				
					if(m_Graphic)
					{
						ClearArea(m_ChBoard);
						for(i=0;i<=m_ChBoard-1;i++)
						{
							PlaceQueen(m_ChBoard,i,Sample.ChromosomeMatrix[i][0]);
							FillMatrix[i]=Sample.ChromosomeMatrix[i][0];
						}
							
						if(m_Graphic && m_Animate)
							Sleep(500);
						
					}
				
				Sample.GenerateCrossOverMatrix();	
				
				Sample.Mating();

				Sample.ApplyMutation();

				
				

			}
		
		
			gs="";
			for (i=0;i<=m_ChBoard-2;i++)
			{
				as.Format("%d_",Sample.ChromosomeMatrix[i][0]);
				gs+=as;
			}
			as.Format("%d",Sample.ChromosomeMatrix[m_ChBoard-1][0]);
			gs+=as;
			
			m_BestAnswer=gs;
			
			gs.Format("%d",Sample.CostMatrix[0]);
			m_BestCost=gs;

			m_Generation=num;
					
			UpdateData(0);

		if (m_BestDisplay && !m_Graphic)
		{
			InitializeBoard(m_ChBoard);
			ClearArea(m_ChBoard);
			for(i=0;i<=m_ChBoard-1;i++)
			{
				PlaceQueen(m_ChBoard,i,Sample.ChromosomeMatrix[i][0]);
				FillMatrix[i]=Sample.ChromosomeMatrix[i][0];
			}
			
		}
	}
	else
	{
		MessageBox("Error");
	}

	
}

