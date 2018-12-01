// ChessDlg.h : header file
//

#if !defined(AFX_CHESSDLG_H__E409357F_B779_484F_9265_40456CEE6892__INCLUDED_)
#define AFX_CHESSDLG_H__E409357F_B779_484F_9265_40456CEE6892__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
#include "GAQueen.h"
/////////////////////////////////////////////////////////////////////////////
// CChessDlg dialog

class CChessDlg : public CDialog
{
// Construction
public:
	CChessDlg(CWnd* pParent = NULL);	// standard constructor
	
	void PlaceQueen(int index,int row,int column);
	void ClearArea(int index);
	void InitializeBoard(int index);

	//CString	m_Iteration;
	int FillMatrix[30];

// Dialog Data
	//{{AFX_DATA(CChessDlg)
	enum { IDD = IDD_CHESS_DIALOG };
	CStatic	m_myStatic;
	int		m_Iteration;
	int		m_Population;
	float   m_MutationRate;
	int		m_ChBoard;
	BOOL	m_Animate;
	BOOL	m_Graphic;
	BOOL	m_BestDisplay;
	CString	m_BestAnswer;
	CString	m_BestCost;
	int		m_Generation;


	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CChessDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	

	// Generated message map functions
	//{{AFX_MSG(CChessDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	virtual void OnOK();
	afx_msg void OnStart();
//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_CHESSDLG_H__E409357F_B779_484F_9265_40456CEE6892__INCLUDED_)
