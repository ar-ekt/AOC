print(*(lambda stacks_raw, procedure_raw, recursive_lambda, move_from_stack, rearrangement: (lambda stacks, procedure: (recursive_lambda(rearrangement, move_from_stack, stacks, procedure, stay_in_order, 0) for stay_in_order in (False, True)))([list(filter(bool, (stacks_raw[floor_index][stack_index*4:stack_index*4+4][1].strip() for floor_index in range(len(stacks_raw)-2, -1, -1)))) for stack_index in range(len(stacks_raw[0]) // 4 + 1)], list(map(lambda step: list(map(int, step.split()[1::2])), procedure_raw))))(*map(str.splitlines, open('Day05.txt').read().split('\n\n')), lambda f, *p: f(f, *p), lambda stack, stay_in_order: stack if stay_in_order else stack[::-1], lambda rearrangement, move_from_stack, stacks, procedure, stay_in_order, step_index: ''.join(stack[-1] for stack in stacks) if len(procedure) == step_index else rearrangement(rearrangement, move_from_stack, [stack + move_from_stack(stacks[procedure[step_index][1]-1][-procedure[step_index][0]:], stay_in_order) if index == procedure[step_index][2]-1 else stack[:-procedure[step_index][0]] if index == procedure[step_index][1]-1 else stack for index, stack in enumerate(stacks)], procedure, stay_in_order, step_index+1)), sep='\n')
