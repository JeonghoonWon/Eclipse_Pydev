package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame04 frame = new MyFrame04();
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
	public MyFrame04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setText("1");
		tf1.setBounds(12, 100, 47, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setText("2");
		tf2.setColumns(10);
		tf2.setBounds(145, 100, 47, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setColumns(10);
		tf3.setBounds(326, 100, 47, 21);
		contentPane.add(tf3);
		
		JLabel lbl = new JLabel("에서");
		lbl.setBounds(86, 103, 47, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("까지 합은");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String a = tf1.getText();
				String b = tf2.getText();
				
				int aa = Integer.parseInt(a);
				int bb = Integer.parseInt(b);
				
				int sum = 0;
				for(int i=aa; i<=bb;i++) {
					sum += i;
					
				}
	
				tf3.setText(sum+"");
				
			}
		});
		btn.setBounds(220, 99, 97, 23);
		contentPane.add(btn);
	}

}
