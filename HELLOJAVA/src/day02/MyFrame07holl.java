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

public class MyFrame07holl extends JFrame {

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
					MyFrame07holl frame = new MyFrame07holl();
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
	public MyFrame07holl() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblCom = new JLabel("컴 :");
		lblCom.setBounds(32, 42, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblMine = new JLabel("나 :");
		lblMine.setBounds(32, 91, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblResult = new JLabel("결과 :");
		lblResult.setBounds(32, 142, 57, 15);
		contentPane.add(lblResult);
		
		tfCom = new JTextField();
		tfCom.setBounds(105, 39, 116, 21);
		contentPane.add(tfCom);
		tfCom.setColumns(10);
		
		tfMine = new JTextField();
		tfMine.setColumns(10);
		tfMine.setBounds(105, 88, 116, 21);
		contentPane.add(tfMine);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(105, 139, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("실행하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myexecute();
				
				}
		});
		btn.setBounds(24, 180, 197, 23);
		contentPane.add(btn);
	}
	
	public void myexecute() {
		String com = "";
		String mine =tfMine.getText();
		String result = "";
		
		double rnd = Math.random();
		
		if(rnd > 0.5) {
			com = "홀";
		}else {
			com = "짝";
		}
		
		if(com.equals(mine)) {
			result = "이김";
		}else {
			result = "짐";
		}
	
		tfCom.setText(com);
		tfResult.setText(result);
		
	}

}
