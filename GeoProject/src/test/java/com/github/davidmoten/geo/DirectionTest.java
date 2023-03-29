package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;

import static org.junit.Assert.*;

@RunWith(Parameterized.class)
public class DirectionTest {
    public Direction direction, expected;

    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{{Direction.RIGHT, Direction.LEFT},{Direction.LEFT, Direction.RIGHT},{Direction.BOTTOM, Direction.TOP},{Direction.TOP, Direction.BOTTOM}});
    }

    public DirectionTest(Direction d, Direction e) {
        this.direction = d;
        this.expected = e;
    }

    @Test
    public void opposite() throws Exception {
        direction = direction.opposite();
        assertEquals(expected, direction);
    }
}

/* //Lab 1
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
*/