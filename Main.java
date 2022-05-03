package com.company;

public class Main {

    public static void main(String[] args) {
	printMegaBytesandKiloBytes(2500);
    printMegaBytesandKiloBytes(-1024);
    printMegaBytesandKiloBytes(5000);
    }
    public static void printMegaBytesandKiloBytes(int kilobytes){
        if (kilobytes<0){
            System.out.println("Invalid Value");
        }
        else if (kilobytes>0){
            int xx=kilobytes;
            int yy= kilobytes/1024;
            int zz=  kilobytes % 1024;

            System.out.println(xx+"KB = "+yy+" MB and "+zz+" KB");
        }

    }
}
