/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Joao Paulo Zinga																            x/
/x		        Numero: 13678																		            x/
/x		        Data: 01/06/2018																	            x/
/x		        Descrição: Classe de XJFrame, Classe que estende uma JFrame!					  		      	x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

	package XJComponents;

    import javax.swing.JOptionPane;
    import java.util.ArrayList;
    import javax.swing.ImageIcon;
    import javax.swing.JFrame;
    import javax.swing.JComponent;
    import javax.swing.JLabel;
    import javax.swing.Action;
	import javax.swing.AbstractAction;
    import java.awt.Insets;
    import java.awt.Container;
    import java.awt.Graphics;
    import java.awt.GridBagLayout;
    import java.awt.GridBagConstraints;
    import java.awt.event.ActionEvent;
	
 	
	public class XJFrame extends JFrame
	{
		private XJMenuBar menuBar;	
		private boolean activeMenuBar;
		private JLabel backgroundImageJLB;
		private Container container;
		private ArrayList<JComponent> components = new ArrayList<JComponent>();
		
		public Action logOutAction;
		public Action exitAction;
		
		public XJFrame()
		{
			setLayout(new GridBagLayout());
			defaultActions();
			container = getContentPane();
		}
		
		public void setActiveMenuBar(boolean activeMenuBar, int modo)
		{
			if (activeMenuBar)
			{
				if (modo == XDefs.DEFAULT)
				{
					menuBar = new XJMenuBar(new String[]{"Ficheiro"});
					menuBar.getMenu(0).addItem("LogOut");
					menuBar.getMenu(0).addItem("Sair");
					menuBar.getMenu(0).getItem(0).setAction(logOutAction);
					menuBar.getMenu(0).getItem(1).setAction(exitAction);
				}
				else
				{
					menuBar = new XJMenuBar();
				}
				setJMenuBar(menuBar);
			}
			this.activeMenuBar = activeMenuBar;
		}
		
		public XJMenuBar getJXMenuBar()
		{
			return menuBar;
		}
		
		public void setBackgroundImage(ImageIcon imageIcon)
		{
			backgroundImageJLB = new JLabel(imageIcon);
			container.add(backgroundImageJLB, new GridBagConstraints(0,0,9,9,0,0, GridBagConstraints.CENTER, GridBagConstraints.NONE, new Insets(0,0, 0,1),0,0));  
		}
		
		public void refreshBackgroundImage(ImageIcon imageIcon)
	    {
	    	container.remove(backgroundImageJLB);
	    	container = getContentPane();	
	    	backgroundImageJLB = new JLabel(imageIcon);
			container.add(backgroundImageJLB, new GridBagConstraints(0,0,9,9,0,0, GridBagConstraints.CENTER, GridBagConstraints.NONE, new Insets(0,0, 0,1),0,0));  
			container.revalidate();	    
	    }
		
		public void addComponent(JComponent element,int positionX, int positionY, int largura, int altura)
	    {
	    	container.add(element, new GridBagConstraints(0,0,0,0,0,0,GridBagConstraints.NORTHWEST,GridBagConstraints.NONE,new Insets(positionY,positionX, this.getWidth(),this.getHeight()),largura,altura) );	
	    	components.add(element);
	    }
	    
	    public void refreshComponent(JComponent element,int positionX, int positionY, int largura, int altura)
	    {
	    	container.remove(element);
	    	container = getContentPane();	
	    	container.add(element, new GridBagConstraints(0,0,0,0,0,0,GridBagConstraints.NORTHWEST,GridBagConstraints.NONE,new Insets(positionY,positionX, 500,500),largura,altura) );	
			container.revalidate();	    
	    }
	    
	    public JComponent getComponent(JComponent comp)
	    {
	    	int stopNumber = components.size();
	    	JComponent componentI = null;
            for (int i = 0; i < stopNumber; i++)
            {
            	componentI = components.get(i); 
            	if (comp == componentI)
            	{
            		System.out.println("Componente encontrado");
            		return componentI;
            	}
            	
            }
            System.out.println("Componente nao encontrado");//JOptionPane.showMessageDialog(null, "Componente nao encontrado");
            return componentI; 
	    }
	    
	    public void defaultActions()
	    {
	    	logOutAction = new AbstractAction() 
			{
				public void actionPerformed( ActionEvent event ) 
				{ 
					dispose();
				}
		  	};
		  	logOutAction.putValue( Action.NAME, "LogOut");
		  	logOutAction.putValue( Action.SHORT_DESCRIPTION, "Sair do sistema" );
		  	
		  	exitAction = new AbstractAction() 
			{
				public void actionPerformed( ActionEvent event ) 
				{ 
					System.exit(0);
				}
		  	};
		  	exitAction.putValue( Action.NAME, "Sair");
		  	exitAction.putValue( Action.SHORT_DESCRIPTION, "Voltar a tela de Login" );
	    }
	}
