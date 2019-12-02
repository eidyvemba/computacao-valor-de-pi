/*xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/
/x																							                    x/
/x		        Autor: Joao Paulo Zinga																            x/
/x		        Numero: 13678																		            x/
/x		        Data: 11/06/2018																	            x/
/x		        Descrição: Classe de XJSensor que estende uma JTextArea  										x/
/x			                                    											                    x/
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx*/

	package XJComponents;
	
    import javax.swing.JTextArea;
    import java.awt.event.MouseListener;
    import java.awt.event.MouseMotionListener;

    public class XJSensor extends JTextArea
    {
    	
    	public XJSensor()
    	{
    		//super("");
    		setEditable(false);
			setOpaque(false);
    	}
    	
    	public XJSensor(MouseListener handler1, MouseMotionListener handler2)
    	{
    		super("");
    		setEditable(false);
			setOpaque(false);
			addMouseListener(handler1);
			addMouseMotionListener(handler2);
    	}
    }
