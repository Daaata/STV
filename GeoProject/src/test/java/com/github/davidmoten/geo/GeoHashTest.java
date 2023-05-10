package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.awt.*;
import java.util.*;
import java.util.List;

import static org.junit.Assert.*;
import static org.junit.runners.Parameterized.*;

@RunWith(Parameterized.class)
public class GeoHashTest {

    public int leftlat, leftlon, rightlat, rightlon, length;
    public String text;
    public CoverageLongs coveragelongs;

    @Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{{0,0,0,0}, {-90,-180,-90,-180}, {90,180,90,180}});
        /*{90,180,90,180}, {90,180,90,-180}, {90,180,90,0},
                                            {90,180,-90,180}, {90,180,-90,-180}, {90,180,-90,0},
                                            {90,180,0,180}, {90,180,0,-180}*/
    }

    public GeoHashTest(int lt, int ln, int rt, int rn) {
        this.leftlat = lt;
        this.leftlon = ln;
        this.rightlat = rt;
        this.rightlon = rn;
        this.length = 12;
        this.text = "29jw";
        this.coveragelongs = GeoHash.coverBoundingBoxLongs(leftlat,leftlon,rightlat,rightlon,length);
    }

    @Test
    public void hashLengthToCoverBoundingBox() throws Exception {
        assertEquals(length,GeoHash.hashLengthToCoverBoundingBox(leftlat,leftlon,rightlat,rightlon));
    }

    @Test
    public void coverBoundingBoxLongs() throws Exception {
        GeoHash.coverBoundingBox(0,0,0,0);
        GeoHash.coverBoundingBox(0,0,0,0,1);
        GeoHash.gridAsString("",0,0,0,0);
        assertEquals(length,coveragelongs.getHashLength());
    }

    @Test
    public void encodeHash() throws Exception {
        String line = GeoHash.encodeHash(1,1,2);
        assertEquals("s0", line);
        line = GeoHash.encodeHash(1,1);
        assertEquals("s00twy01mtw0", line);
        LatLong latlong = new LatLong(1,1);
        line = GeoHash.encodeHash(latlong,2);
        assertEquals("s0", line);
        line = GeoHash.encodeHash(latlong);
        assertEquals("s00twy01mtw0", line);
    }

    @Test
    public void encodeHashToLong() throws Exception {
        long l = GeoHash.encodeHashToLong(3,2,1);
        assertEquals(-4611686018427387903L,l);
    }

    @Test
    public void hashContains() throws Exception {
        assertEquals(true,GeoHash.hashContains("s0",1,1));
    }

    @Test(expected = IllegalArgumentException.class)
    public void neighbours() throws Exception {
        String[] e = {"29jq", "29jy", "29jx", "29jt", "29jr", "29jm", "29jz", "29jv"};
        String[] a = GeoHash.neighbours(text).toArray(new String[0]);
        assertEquals(e,a);
        e = new String[]{"-29jt", "-29jx", "-29jy", "-29jq", "-29jv", "-29jm", "-29jz", "-29jr"};
        a = GeoHash.neighbours("-29jw").toArray(new String[0]);
        assertEquals(e,a);
        GeoHash.neighbours("").toArray(new String[0]);
    }

    @Test(expected = IllegalArgumentException.class)
    public void adjacentHash() throws Exception {
        //29jw
        String line = GeoHash.adjacentHash(text, Direction.BOTTOM,1);
        assertEquals("29jt", line);
        line = GeoHash.adjacentHash(text, Direction.BOTTOM,0);
        assertEquals(text, line);
        line = GeoHash.adjacentHash(text, Direction.TOP,1);
        assertEquals("29jx", line);
        line = GeoHash.adjacentHash(text, Direction.TOP,0);
        assertEquals(text, line);
        line = GeoHash.adjacentHash(text, Direction.LEFT,1);
        assertEquals("29jq", line);
        line = GeoHash.adjacentHash(text, Direction.LEFT,0);
        assertEquals(text, line);
        line = GeoHash.adjacentHash(text, Direction.RIGHT,1);
        assertEquals("29jy", line);
        line = GeoHash.adjacentHash(text, Direction.RIGHT,0);
        assertEquals(text, line);
        //-29jw
        line = GeoHash.adjacentHash("-29jw", Direction.BOTTOM,1);
        assertEquals("-29jq", line);
        line = GeoHash.adjacentHash("-29jw", Direction.BOTTOM,0);
        assertEquals("-29jw", line);
        line = GeoHash.adjacentHash("-29jw", Direction.TOP,1);
        assertEquals("-29jy", line);
        line = GeoHash.adjacentHash("-29jw", Direction.TOP,0);
        assertEquals("-29jw", line);
        line = GeoHash.adjacentHash("-29jw", Direction.LEFT,1);
        assertEquals("-29jt", line);
        line = GeoHash.adjacentHash("-29jw", Direction.LEFT,0);
        assertEquals("-29jw", line);
        line = GeoHash.adjacentHash("-29jw", Direction.RIGHT,1);
        assertEquals("-29jx", line);
        line = GeoHash.adjacentHash("-29jw", Direction.RIGHT,0);
        assertEquals("-29jw", line);
        //
        GeoHash.adjacentHash("", Direction.BOTTOM,1);
        GeoHash.adjacentHash("", Direction.BOTTOM,0);
        GeoHash.adjacentHash("", Direction.TOP,1);
        GeoHash.adjacentHash("", Direction.TOP,0);
        GeoHash.adjacentHash("", Direction.LEFT,1);
        GeoHash.adjacentHash("", Direction.LEFT,0);
        GeoHash.adjacentHash("", Direction.RIGHT,1);
        GeoHash.adjacentHash("", Direction.RIGHT,0);
        //
        line = GeoHash.adjacentHash(text, Direction.BOTTOM,-1);
        assertEquals("29jt", line);
    }

    @Test(expected = IllegalArgumentException.class)
    public void right() throws Exception{
        assertEquals("29jy", GeoHash.right("29jw"));
        assertEquals("-29jx", GeoHash.right("-29jw"));
        GeoHash.right("");
    }

    @Test(expected = IllegalArgumentException.class)
    public void left() throws Exception{
        assertEquals("29jq", GeoHash.left("29jw"));
        assertEquals("-29jt", GeoHash.left("-29jw"));
        GeoHash.left("");
    }

    @Test(expected = IllegalArgumentException.class)
    public void top() throws Exception{
        assertEquals("29jx", GeoHash.top("29jw"));
        assertEquals("-29jy", GeoHash.top("-29jw"));
        GeoHash.top("");
    }

    @Test(expected = IllegalArgumentException.class)
    public void bottom() throws Exception{
        assertEquals("29jt", GeoHash.bottom("29jw"));
        assertEquals("-29jq", GeoHash.bottom("-29jw"));
        GeoHash.bottom("");
    }

    @Test
    public void fromLongToString() throws Exception {
        try{
            GeoHash.fromLongToString(12);
        }catch(IllegalArgumentException e){
            assertEquals(e.getMessage(),"invalid long geohash 12");
        }
        try{
            GeoHash.fromLongToString(0);
        }catch(IllegalArgumentException e){
            assertEquals(e.getMessage(),"invalid long geohash 0");
        }
        String s = GeoHash.fromLongToString(1);
        assertEquals(s,"0");
    }

    @Test
    public void heightDegrees() throws Exception {
        assertEquals(180, GeoHash.heightDegrees(0), 0.001);
        assertEquals(0, GeoHash.heightDegrees(13), 0.001);
    }
}

/* //Lab 1//
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

    @Test
    public void encodeHash() throws Exception {
        String line = GeoHash.encodeHash(1,1,2);
        assertEquals("s0", line);
    }

    @Test
    public void hashContains() throws Exception {
        assertEquals(true,GeoHash.hashContains("s0",1,1));
    }

}
*/