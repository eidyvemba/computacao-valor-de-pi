/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Joao Paulo Zinga																            x/
/x		        Numero: 13678																		            x/
/x		        Data: 01/06/2018																	            x/
/x		        Descrição: Classe de XJMenu que estende JMenu!									        		x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

	package XJComponents;
	
	import java.util.ArrayList;
	import javax.swing.JMenuBar;
    import javax.swing.JMenu;
    import javax.swing.JMenuItem;
    import java.awt.Color;
    import java.awt.Font;
    import java.awt.Graphics;
    
	public class XJMenu extends JMenu
    {
        private ArrayList<JMenuItem> item = new ArrayList<JMenuItem>();
        private int numberOfItems;

		// Construtor da classe XJMenu que recebe a descricao do XJMenu //
        public XJMenu(String Description)
        {
            super(Description);   
        }
        
        // Construtor da classe XJMenu que recebe a descricao do XJMenu e um arrayList com a descricao dos itens desse XJMenu //
        public XJMenu(String Description, String itemDescription[])
        {
            new XJMenu(Description); 
            addItem(itemDescription);  
        }
        
        // Metodo que recerbe uma String com a descricao dos itens do XJMenu cria-os e adiciona-os ao XJMenu //
        public void addItem(String itemDescription)
        {
            item.add(new JMenuItem(itemDescription));
			formatarTexto(item.get(numberOfItems), getForeground(), getFont());
			add(item.get(numberOfItems));
			numberOfItems++;
        }
        
        // Metodo que recerbe um array de String's com a descricao dos itens do XJMenu cria-os e adiciona-os ao XJMenu //
        public void addItem(String itemDescription[])
        {
            int stopNumber = itemDescription.length;
            for (int i = 0; i < stopNumber; i++)
            	addItem(itemDescription[i]);
        }
        
        // Metodo que recerbe um arrayList com a descricao dos itens do XJMenu cria-os e adiciona-os ao XJMenu //
        private void formatarTexto(JMenuItem item, Color cor, Font fonte)
        {
		    item.setFont(fonte);
            item.setForeground(cor);
        }
        
        // Metodo que retorna uma referencia a um Item de um XJMenu em uma determinada posicao //
        public JMenuItem getItem(int x)
        {
        	return item.get(x);
        }
        
        // Funcao que retorna o numero de itens  //
        public int getNumbersOfItems()
        {
        	return numberOfItems;
        }
    }
