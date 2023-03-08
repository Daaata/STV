package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class GeoHashTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void adjacentHash() throws Exception {
        String line = GeoHash.adjacentHash("29jw", Direction.BOTTOM,1);
        assertEquals("29jt", line);
    }

    @Test
    public void neighbours() throws Exception {
        List<String> list = GeoHash.neighbours("29jw");
        assertEquals("29jq", list.get(0));
    }

    @Test
    public void encodeHashToLong() throws Exception {
        long l = GeoHash.encodeHashToLong(3,2,1);
        assertEquals(-4611686018427387903L,l);
    }

    @Test
    public void hashLengthToCoverBoundingBox() throws Exception {
        int i = GeoHash.hashLengthToCoverBoundingBox(2,2,1,1);
        assertEquals(2,i);
    }

    @Test
    public void coverBoundingBoxLongs() throws Exception {
        CoverageLongs cl = GeoHash.coverBoundingBoxLongs(0.1,0.1,0.1,0.1,1);
        int length = cl.getHashLength();
        assertEquals(1,length);
    }

}