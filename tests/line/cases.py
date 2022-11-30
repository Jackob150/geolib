directional_line_cases = [([0,0],[(0,-1,0)]),
                          ([1,1],[(1,-1,1)]),
                          ([-1,3],[(-1,-1,3)]),]

two_points_line_cases = [([(0,0),(0,0)],[None]),
                         ([(1,1),(1,1)],[None]),
                         ([(0,0),(1,1)],[(1,-1,0)]),
                         ([(1,2),(2,1)],[(1,1,-3)]),]

vector_line_cases = [([(0,0),(0,0)],[None]),
                     ([(0,0),(1,0)],[(0,1,0)]),
                     ([(0,0),(0,1)],[(1,0,0)]),
                     ([(0,0),(1,1)],[(1,-1,0)]),
                     ([(-1,2),(1,-1)],[(1,1,-1)]),]

is_point_in_line_cases = [([(0,0),(0,1,0)],True),
                          ([(0,0),(0,1,1)],False),
                          ([(0.001,0),(1,0,0)],False),
                          ([(2,4),(2,-1,0)],True),
                          ([(-1,-5),(2,3,17)],True),
                          ([(-2,3),(1,1,1)],False),]

get_direction_cases = [([(0,1,0)],[(-1,0)]),
                       ([(1,0,0)],[(0,1)]),
                       ([(1,-1,0)],[(1,1)]),
                       ([(3,-2,5)],[(2,3)]),
                       ([(-2,1,-10)],[(-1,-2)]),]

get_gradient_cases = [([(0,1,0)],0),
                      ([(1,0,0)],None),
                      ([(1,1,0)],-1),
                      ([(-1,1,0)],1),
                      ([(-1,-1,2)],-1),
                      ([(12,-30,0)],0.4),]