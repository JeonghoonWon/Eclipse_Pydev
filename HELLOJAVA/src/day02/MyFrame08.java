package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame08 extends JFrame {

	private JPanel contentPane;
	private JTextField tfCom;
	private JTextField tfMine;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame08 frame = new MyFrame08();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyFrame08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblCom = new JLabel("컴 :");
		lblCom.setBounds(32, 37, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblMine = new JLabel("나 :");
		lblMine.setBounds(32, 77, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblResult = new JLabel("결과 :");
		lblResult.setBounds(32, 124, 57, 15);
		contentPane.add(lblResult);
		
		tfCom = new JTextField();
		tfCom.setBounds(89, 34, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfMine = new JTextField();
		tfMine.setColumns(10);
		tfMine.setBounds(89, 74, 116, 21);
		contentPane.add(tfMine);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(89, 121, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("실행하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				startgame();
			}
		});
		btn.setBounds(32, 164, 97, 23);
		contentPane.add(btn);
	}

	public void startgame() {
		String com = "";
		String mine = tfMine.getText();
		String result = "";
		
		double rnd = Math.random();
		
		if(rnd <0.33) {
			com = "가위";
		}else if (rnd < 0.66) {
			com = "바위";
		}else {
			com = "보";
		}
		
		if(com.equals(mine)) {
			result = "비김";
		}else if (com.equals("가위") && mine.equals("바위")||com.equals("바위") && mine.equals("보")||com.equals("보") && mine.equals("가위")) {
			result = "이김";
		}else {
			result = "짐";
		}
		
		tfCom.setText(com);
		tfResult.setText(result);
	}
	
}
