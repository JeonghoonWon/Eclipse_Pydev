package day02;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MyFrame06 extends JFrame {

	private JPanel contentPane;
	private JTextField tfDan;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame06 frame = new MyFrame06();
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
	public MyFrame06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JTextArea ta = new JTextArea();
		ta.setBounds(12, 10, 166, 230);
		contentPane.add(ta);
		
		tfDan = new JTextField();
		tfDan.setText("2");
		tfDan.setBounds(200, 38, 39, 21);
		contentPane.add(tfDan);
		tfDan.setColumns(10);
		
		JButton btn = new JButton("출력");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				String dan = tfDan.getText();
				int int_dan = Integer.parseInt(dan);
				
				String txt ="";
				txt += dan+"*1="+(int_dan*1)+"\n";
				txt += dan+"*2="+(int_dan*2)+"\n";
				txt += dan+"*3="+(int_dan*3)+"\n";
				txt += dan+"*4="+(int_dan*4)+"\n";
				txt += dan+"*5="+(int_dan*5)+"\n";
				txt += dan+"*6="+(int_dan*6)+"\n";
				txt += dan+"*7="+(int_dan*7)+"\n";
				txt += dan+"*8="+(int_dan*8)+"\n";
				txt += dan+"*9="+(int_dan*9)+"\n";
								
				ta.setText(txt);
				
			}
		});
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btn.setBounds(200, 95, 63, 23);
		contentPane.add(btn);
	}

}
