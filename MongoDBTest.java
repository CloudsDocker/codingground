package com.todzhang;

import com.mongodb.DB;
import com.mongodb.DBCursor;
import com.mongodb.MongoClient;

public class MongoDBTest {

	private static final String HOST="130.49.140.38";
	private static final int PORT=5255;
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		MongoClient client=new MongoClient(HOST,PORT);
		DB db=client.getDB("sampledb");
		System.out.println("=== successfully connect to mongoDB===");
		System.out.println("count is:"+db.getCollection("users").count());
		DBCursor cur= db.getCollection("users").find();
		while(cur.hasNext()){
			System.out.println("---:"+cur.next().toString());
		}
	}

}
