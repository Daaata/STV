package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CoverageLongsTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getHashLength() throws Exception {
        long[] l = {3};
        CoverageLongs c = new CoverageLongs(l,1,3);
        int length = c.getHashLength();
        assertEquals(3, length);
        l = new long[]{};
        c = new CoverageLongs(l,0,3);
        length = c.getHashLength();
        assertEquals(0,length);
    }

    @Test
    public void TesttoString() throws Exception {
        long[] l = {1};
        CoverageLongs c = new CoverageLongs(l,1,3);
        String line = c.toString();
        assertNotEquals("Coverage [hashes="+c.getHashes()+", ratio="+c.getRatio()+"]", line);
    }

    @Test
    public void getCount() throws Exception {
        long[] l = {1};
        CoverageLongs c = new CoverageLongs(l,1,3);
        int count = c.getCount();
        assertEquals(1,count);
    }

}