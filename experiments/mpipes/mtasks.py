from radical import pilot as rp, utils as ru

def prepare_pilot(rd):
    session = rp.Session()
    pmgr = rp.PilotManager(session=session)
    umgr = rp.UnitManager(session=session) 

    pilot = pmgr.submit_pilots(
            rp.ComputePilotDescription(rd))

    umgr.add_pilots(pilot)
    return session, pmgr, umgr

def gen_units(loop_count=1, exec_second=10):
    cuds = []
    for i in range(int(loop_count)):
        cud = rp.ComputeUnitDescription()
        cud.executable    = '/bin/sleep {}'.format(exec_second)
        cud.cpu_processes = 1
        cuds.append(cud)
    return cuds

def set_ratio(prop_per_task={"1:1:1":"10,100,1000"}):
    ntask = []
    for k, v in prop_per_task.items():
        for loop_count, exec_second in zip(k.split(":"), v.split(",")):
            ntask += gen_units(loop_count, exec_second)
    return ntask


if __name__ == '__main__':


    rp_resource_description = {
            'resource'      : "ornl.summit",
            'runtime'       : 30,  # pilot runtime (min)
            'exit_on_error' : True,
            'project'       : "CSC393",
            'queue'         : "batch",
            'access_schema' : "local",
            'cores'         : 168
            }

    session, _, umgr = prepare_pilot(rp_resource_description)
    cuds = set_ratio({"1:1:1": "10,100,1000"})
    umgr.submit_units(cuds)
    umgr.wait_units()
    session.close()