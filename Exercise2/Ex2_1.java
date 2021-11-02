package ex2;

import java.util.ArrayList;

public class Ex2_1_Thread {

	public static void main(String args[])  {
	
		ArrayList<Integer> num = new ArrayList<Integer>();
				
		Ex2_1 rn  = new Ex2_1 ();
		Ex2_1 rn1  = new Ex2_1 ();
		Ex2_1 rn2  = new Ex2_1 ();
		Ex2_1 rn3  = new Ex2_1 ();
		Ex2_1 rn4  = new Ex2_1 ();

	    Thread t1 = new Thread(rn);
	    Thread t2 = new Thread(rn1);
	    Thread t3 = new Thread(rn2);
	    Thread t4 = new Thread(rn3);
	    Thread t5 = new Thread(rn4);

	    t1.start();
	    t2.start();
	    t3.start();
	    t4.start();
	    t5.start();    
	    
	    try {
	        t1.join();
	        t2.join();
	        t3.join();
	        t4.join();
	        t5.join();
	       
	        num.add(rn.getValue());
	        num.add(rn1.getValue());
	        num.add(rn2.getValue());
	        num.add(rn3.getValue());
	        num.add(rn4.getValue());
	        
	        int sum = 0;
			for (int i = 0; i < num.size(); i++) {
				    sum += num.get(i);
			    }	       			
		    System.out.print("\nSum of random number is :: " + sum);
	        
	    } catch (InterruptedException e) {
	        e.printStackTrace();
	    }
  
	    		
}
	
}