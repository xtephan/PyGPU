__kernel void part1(__global float* c)
{
    unsigned int gid = get_global_id(0);

	c[gid] = gid;
 
}