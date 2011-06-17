__kernel void part1(__global int* result)
{
    unsigned int gid = get_global_id(0);
	unsigned int div;
	unsigned int ok=1;

	for(div=2; div<=gid/2; div++) {
	
		if( (gid%div)==0 ) {
			ok=0;
		}
	
	}
	
	if(ok) {
		result[gid]=1;
	} else {
		result[gid]=0;
	}

	
}