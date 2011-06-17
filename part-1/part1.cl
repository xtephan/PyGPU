__kernel void part1(__global float* a, __global float* b, __global float* c)
{
    unsigned int gid = get_global_id(0);

    
	c[gid] = a[gid] + b[gid];
	c[gid] = c[gid] * (a[gid] + b[gid]);
	c[gid] = c[gid] * (a[gid] / 2.0);
    
    
}