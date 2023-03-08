package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class DirectionTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void opposite() throws Exception {
        //Direction.BOTTOM
        Direction direction = Direction.RIGHT;
        direction = direction.opposite();
        assertEquals(Direction.LEFT, direction);
        direction = direction.opposite();
        assertEquals(Direction.RIGHT, direction);
        direction = Direction.TOP;
        direction = direction.opposite();
        assertEquals(Direction.BOTTOM, direction);
        direction = direction.opposite();
        assertEquals(Direction.TOP, direction);
    }
}