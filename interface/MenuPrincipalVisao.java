/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Joao Paulo Zinga																            x/
/x		        Numero: 13678																		            x/
/x		        Data: 01/06/2018																	            x/
/x		        Descrição: Classe de MenuPrincipalVisao, visao principal do programa!					        x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

	import javax.swing.JComponent;
    import javax.swing.ImageIcon;
    import javax.swing.JLabel;
    import javax.swing.JFrame;
    import javax.swing.JDialog;
    import javax.swing.JTextArea;
    import javax.swing.JTextField;
    import javax.swing.JButton;
    import javax.swing.JMenuBar;
    import javax.swing.JMenu;
    import javax.swing.JMenuItem;
    import javax.swing.JPanel;
    import javax.swing.Action;
	import javax.swing.AbstractAction;
    import java.awt.Insets;
    import java.awt.Color;
    import java.awt.GradientPaint;
    import java.awt.Font;
    import java.awt.Container;
    import java.awt.Graphics;
    import java.awt.GridBagLayout;
    import java.awt.GridBagConstraints;
    import java.awt.event.MouseEvent;
    import java.awt.event.MouseListener;
    import java.awt.event.MouseMotionListener;
    import java.awt.event.ActionEvent;
    import java.awt.event.ActionListener;
    
    import XJComponents.XJMenuBar;
    import XJComponents.XJMenu;
    import XJComponents.XJFrame;
    import XJComponents.XDefs;

	public class MenuPrincipalVisao extends XJFrame
	{
		private String menuNames[];
		private XJMenuBar menuBar;
		private JTextField searchJT;
		private TextPrompt searchJTMask;
		private String model;
		private Font menuFont;
		private Color menuBackgroundColor;
		private Color menuForegroundColor;
		
		//public Action assignAction;
	
		public MenuPrincipalVisao()
		{	
			createComponents();
        	setUndecorated(true);
        	pack();
        	setVisible(true);
        	setLocationRelativeTo(null);
		}
		
	    private void createComponents()
	    {
	    
	    	setActiveMenuBar(true, XDefs.NOT_DEFAULT);
			menuBar = getJXMenuBar();
			menuFont = new Font("Time New Roman",Font.PLAIN,14) ;
			menuBackgroundColor = new Color(190,190,240);
			menuForegroundColor = new Color(0,0,0);
			
			setBackgroundImage(new ImageIcon("MenuPrincipal2.png"));
			
			menuNames = new String[]{"Graficos	", "Tabelas", "Sair"};
			menuBar.addMenu(menuNames, menuForegroundColor, menuFont);
			menuBar.getMenu(0).addItem(new String[]{"Serial Pi / Tempo Exec."});
			menuBar.getMenu(0).addItem(new String[]{"Processos Pi / Tempo Exec."});
			menuBar.getMenu(0).addItem(new String[]{"Threads Pi / Tempo Exec."});
			menuBar.getMenu(0).addItem(new String[]{"Lambert Pi / Tempo Exec."});
			menuBar.getMenu(0).addItem(new String[]{"Leibniz Pi / Tempo Exec."});
			menuBar.getMenu(0).addItem(new String[]{"Viete Pi / Tempo Exec."});
			menuBar.getMenu(0).addItem(new String[]{"Nilankantha Pi / Tempo Exec."});
			
			menuBar.getMenu(1).addItem(new String[]{"Serial Pi / Tempo Exec."});
			menuBar.getMenu(1).addItem(new String[]{"Processos Pi / Tempo Exec."});
			menuBar.getMenu(1).addItem(new String[]{"Threads Pi / Tempo Exec."});
			menuBar.getMenu(1).addItem(new String[]{"Lambert Pi / Tempo Exec."});
			menuBar.getMenu(1).addItem(new String[]{"Leibniz Pi / Tempo Exec."});
			menuBar.getMenu(1).addItem(new String[]{"Viete Pi / Tempo Exec."});
			menuBar.getMenu(1).addItem(new String[]{"Nilankantha Pi / Tempo Exec."});
			
			menuBar.getMenu(2).addItem(new String[]{"Sair"});
			menuBar.getMenu(2).getItem(0).setAction(exitAction);
			
			
		}

	}

