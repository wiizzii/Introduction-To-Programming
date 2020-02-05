import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;

public class SudokuGUI extends JFrame{
	Field field = new Field();
	Sudoku sudoku = new Sudoku();
	int[][] board = field.getBoard();
	int x = 0;
	private JFrame Frame;
	private JPanel controlPanel;
	private JTextField notCleared = new JTextField();
    private JTextField tf[][]= new JTextField[9][9];
    private JPanel panel[][]= new JPanel [3][3];

    public SudokuGUI(){
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                tf[i][j]=new JTextField(1);
            }
        }

        for(int x=0; x<3; x++){
            for(int z=0; z<3; z++){
                panel[x][z]=new JPanel(new GridLayout(3,3));
            }
        }
        PrepareGUI();
        BtnDisplay();
    }
    
    public static void main(String[] args){
		
		SudokuGUI win = new SudokuGUI();
		win.ShowGroupLayout();
	}
		
	private void PrepareGUI(){
		Frame = new JFrame("SudokuGUI");
		Frame.setSize(500,500);
		Frame.setResizable(false);
		
		notCleared.setHorizontalAlignment(JTextField.CENTER);
		notCleared.setFont(new Font("Monospaced", Font.BOLD, 15));
		notCleared.setEditable(false);
		
		controlPanel = new JPanel();
		controlPanel.setLayout(new FlowLayout());
		
		GridBagLayout layout = new GridBagLayout();
		Frame.setLayout(layout);        
		GridBagConstraints gbc = new GridBagConstraints();

		gbc.fill = GridBagConstraints.HORIZONTAL;
		gbc.gridx = 0;
		gbc.gridy = 0;
		Frame.add(controlPanel,gbc);

		gbc.gridx = 0;
		gbc.gridy = 1;
		Frame.add(notCleared,gbc); 		
		
		Frame.addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent windowEvent){
				System.exit(0);
			}        
		});
				
		Frame.setVisible(true); 
	}

	private void ShowGroupLayout(){
		Container gridPane = getContentPane();
		gridPane.setPreferredSize(new Dimension(400, 400));
		gridPane.setLayout(new GridLayout(3,3,5,5));

		for (int i=0; i<9; i++){
			for(int j=0; j<9; j++){
				tf[i][j].setHorizontalAlignment(JTextField.CENTER);
				tf[i][j].setFont(new Font("Monospaced", Font.BOLD, 20));
				tf[i][j].setEditable(false);
			}
		}

        for(int x=0; x<=2; x++){
            for(int z=0; z<=2; z++){    
                for(int i=0; i<=2; i++ ){
                    for(int j=0; j<=2; j++){
                        panel[x][z].add(tf[i+x*3][j+z*3]);
                    }
                }
            gridPane.add(panel[x][z]);
            }
        }
		controlPanel.add(gridPane);
	}
	
	private void BtnDisplay(){
		JPanel btnPanel = new JPanel();
		JButton openBtn = new JButton("Open");
		JButton solveBtn = new JButton("Solve");
		JButton saveBtn = new JButton("Save");
		JButton clearBtn = new JButton("clear");
		
		openBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				JFileChooser openFile = new JFileChooser();
				
				if(x == 0){
					openFile.showOpenDialog(null);
					field.fromFile(openFile.getSelectedFile().getAbsolutePath());
					x = 1;
					for (int j=0; j<9; j++){
						for(int i=0; i<9; i++){
							if (board[i][j]==0){
								tf[i][j].setBackground(Color.YELLOW);
							}else{
								tf[i][j].setText("" + board[i][j]);
							}
						}
					}
				}else{
					notCleared.setText("Please clear field before loading a new file.");
				}
			}
		});
		
		solveBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				try {
					sudoku.solve(field, 0, 0);
				} catch (SolvedException e) {}
				for (int i=0; i<9; i++){
					for(int j=0; j<9; j++){
						tf[i][j].setText("" + board[i][j]);
					}
				}
			}
		});
		
		saveBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                JFileChooser saveFile = new JFileChooser();
                saveFile.showSaveDialog(null);
                try{
					File file = new File(saveFile.getSelectedFile().getAbsolutePath());
					if (!file.exists()){
						file.createNewFile();
					}
					FileWriter fwrite = new FileWriter(file.getAbsoluteFile());
					BufferedWriter bwrite = new BufferedWriter(fwrite);
					for (int i=0; i<9; i++){
						for(int j=0; j<9; j++){
							bwrite.write(tf[i][j].getText() + " ");							
						}
						bwrite.newLine();
					}	
					bwrite.close();
					
				} catch (IOException e){
					e.printStackTrace();
				}	
            }
        });
		
		clearBtn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				x = 0;
				notCleared.setText(null);
			for (int j=0; j<9; j++){
					for(int i=0; i<9; i++){
						board[i][j] = 0;
						tf[i][j].setText(null);
						tf[i][j].setBackground(null);
					}
				}	
			}
		});
		
		btnPanel.setLayout(new GridLayout(4,1,5,5));
		controlPanel.add(btnPanel);
		btnPanel.add(openBtn);
		btnPanel.add(solveBtn);
		btnPanel.add(saveBtn);
		btnPanel.add(clearBtn);
	}
}
