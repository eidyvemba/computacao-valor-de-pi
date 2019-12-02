/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Joao Paulo Zinga																            x/
/x		        Numero: 13678																		            x/
/x		        Data: 01/06/2018																	            x/
/x		        Descrição: Classe de XJMenuBar que estende JMenuBar!							    	    	x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

	package XJComponents;
	
	import java.util.ArrayList;
	import javax.swing.JComponent;
	import javax.swing.JMenuBar;
    import javax.swing.JMenu;
    import java.awt.Color;
    import java.awt.Font;
    import java.awt.Graphics;
    import javax.swing.plaf.basic.BasicMenuBarUI;
    
	public class XJMenuBar extends JMenuBar
    {
        private ArrayList<XJMenu> menu = new ArrayList<XJMenu>();
        private Color foregroundColor, backgroundColor;
		private Font font;
		private int numbersOfmenus;
        
        // Construtor da classe XJMenuBar que reutiliza o construtor da super classe JMenuBar//
        public XJMenuBar()
        {
            super();
        }
        
        // Construtor da classe XJMenuBar que recebe a cor do XJMenuBar e a cor das letras dos menus do XJMenuBar respectivamente//
		public XJMenuBar(Color backgroundColor, String menuDescription[])
        {
        	this.backgroundColor = backgroundColor;
            new XJMenuBar();
            addMenu(menuDescription);
            setBackgroundColor(backgroundColor);
		}

		// Construtor da classe XJMenuBar que recebe um array com a descricao dos XJMenu's da XJMenuBar//
        public XJMenuBar(String menuDescription[])
        {
        	new XJMenuBar();
        	addMenu(menuDescription);
        }
        
        // Construtor da classe XJMenuBar que recebe um array com a descricao dos XJMenu's da XJMenuBar a cor e a fonte respectivamente//
        public XJMenuBar(String menuDescription[], Color foregroundColor, Font font)
        {
        	new XJMenuBar();
        	this.foregroundColor = foregroundColor;
        	this.font = font;
        	addMenu(menuDescription, foregroundColor, font);
        }
        
        // Construtor da classe XJMenuBar que recebe um array com a descricao dos XJMenu's da XJMenuBar a cores e a fonte respectivamente//
        public XJMenuBar(String menuDescription[], Color backgroundColor, Color foregroundColor, Font fonte)
        {	
        	this.foregroundColor = foregroundColor;
        	this.font = font;
        	addMenu(menuDescription, foregroundColor, fonte);
        	setBackgroundColor(backgroundColor);
        }
		
		// Metodo que recebe uma String com a descricao do XJMenu cria-o e adiciona-o a XJMenuBar//
		public void addMenu(String menuDescription)
        {
            menu.add(new XJMenu(menuDescription));
            add(menu.get(numbersOfmenus));
            numbersOfmenus++;
        }
        
        // Metodo que recebe um array String com as descricoes dos XJMenu's cria-os e adiciona-os a XJMenuBar//
        public void addMenu(String menuDescription[])
        {
        	int stopNumber = menuDescription.length;
            for (int i = 0; i < stopNumber; i++)
            	addMenu(menuDescription[i]);
        }
        
        // Metodo que recebe um array String com as descricoes, cor, e fonte dos XJMenu's cria-os e adiciona-os a XJMenuBar//
        public void addMenu(String menuDescription[], Color foregroundColor, Font fonte)
        {
            int stopNumber = menuDescription.length;
            for (int i = 0; i < stopNumber; i++)
            {
            	addMenu(menuDescription[i]);
            	setForeground(menu.get(i), foregroundColor, fonte);
            }	
        }
        
        // Metodo que recebe uma cor e pinta a XJMenuBar com essa cor//
		public void setBackgroundColor(final Color backgroundColor)
		{
			this.backgroundColor = backgroundColor; 
		    setUI
            (
		     	new BasicMenuBarUI()
		     	{ 
				    public void paint(Graphics g, JComponent c) 
				    { 
					    g.setColor(backgroundColor); 
			     		g.fillRect(0, 0, c.getWidth(), c.getHeight());
			     	}
		     	}
		    );
		}
        
        // Metodo que recbe um XJMenu, uma cor e uma fonte e formata o texto de um XJMenu da XJMenuBar com esses parametros //
        public void setForeground(XJMenu menu, Color color, Font fonte)
        {
        	menu.setFont(fonte);
		    menu.setForeground(color);
        }
         
        // Metodo que recbe uma cor e uma fonte e formata o texto de todos os XJMenu's da XJMenuBar com esses parametros //      
        public void setForeground(Color color, Font fonte)
        {
        	for (int i = 0; i < numbersOfmenus; i++)
            {
                menu.get(i).setFont(fonte);
		    	menu.get(i).setForeground(color);
            }
        }
        
        // Metodo que retorna uma referencia a um XJMenu em uma determinada posicao //
        public XJMenu getMenu(int x)
        {
        	return menu.get(x);
        }
        
        // Funcao que retorna o numero de menus  //
        public int getnumbersOfmenus()
        {
        	return numbersOfmenus;
        }  
    }
