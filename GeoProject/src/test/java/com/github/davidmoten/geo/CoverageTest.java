package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;

public class CoverageTest {

    @Before
    public void setUp() throws Exception {
        Set<String> word = new HashSet<String>();
        word.add("Katayama");
        word.add("Jenjen");
        word.add("not");
        word.add("Chinchin.");
        Coverage c =  new Coverage(word,3);
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getHashes() throws Exception {
        Set<String> word = new HashSet<String>();
        word.add("Katayama");
        word.add("Jenjen");
        word.add("not");
        word.add("Chinchin.");
        Coverage c =  new Coverage(word,4);
        Set<String> hash = c.getHashes();
        assertEquals(word, hash);
    }

    @Test
    public void getRatio() throws Exception {
        Set<String> word = new HashSet<String>();
        word.add("Katayama");
        word.add("Jenjen");
        word.add("not");
        word.add("Chinchin.");
        Coverage c =  new Coverage(word,4);
        double ratio = c.getRatio();
        assertEquals(4.0, ratio,0.001);
    }

    @Test
    public void getHashLength() throws Exception {
        Set<String> word = new HashSet<String>();
        Coverage c =  new Coverage(word,4);
        int length = c.getHashLength();
        assertEquals(0, length);
        word.add("Katayama");
        word.add("Jenjen");
        word.add("not");
        word.add("Chinchin.");
        c =  new Coverage(word,4);
        length = c.getHashLength();
        assertEquals(9, length);
    }

    @Test
    public void getHashLengthUseGraph() throws Exception {
        Set<String> word = new HashSet<String>();
        Coverage c = new Coverage(word, 0);
        int length = c.getHashLength();
        assertEquals(0,length);
        word.add("29jw");
        c = new Coverage(word, 4);
        length = c.getHashLength();
        assertEquals(4,length);
    }

    @Test
    public void TesttoString() throws Exception {
        Set<String> word = new HashSet<String>();
        word.add("Katayama");
        word.add("Jenjen");
        word.add("not");
        word.add("Chinchin.");
        Coverage c =  new Coverage(word,4);
        String line = c.toString();
        assertEquals("Coverage [hashes=[Chinchin., not, Katayama, Jenjen], ratio=4.0]", line);
    }

    @Test
    public void TestCoverage() throws Exception {
        long[] l ={1};
        CoverageLongs cl = new CoverageLongs(l,1,3);
        Coverage c = new Coverage(cl);
    }

}