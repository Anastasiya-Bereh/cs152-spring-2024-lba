prolog_tests = 

'''

% small cafe with vegan options and budget friendly
test_case_1 :-
    %askables with predetermined responses
    retractall(askable(_)), % clean mocks from before
    assert(askable(budget(low))),
    assert(askable(distance(15, 10, _))), 
    assert(askable(wifi(_))), 
    assert(askable(work(_))), 
    assert(askable(vegan(yes))),
    assert(askable(card_payment(_))), 
    assert(askable(size(small))),
    assert(askable(closed_days(_))), 
    recommend_cafe(Name),
    % answer should be Café Le Vent or Café Três
    member(Name, ["Café Le Vent", "Café Três"]),
    write('Test Case 1 Passed: Recommended Cafe is '), write(Name), nl.

%cafe with wifi and card payment option
test_case_2 :-
    retractall(askable(_)), 
    assert(askable(budget(_))), % no budget specified
    assert(askable(distance(_, _, _))), 
    assert(askable(wifi(yes))),
    assert(askable(work(_))), 
    assert(askable(vegan(_))), 
    assert(askable(card_payment(yes))),
    assert(askable(size(large))),
    assert(askable(closed_days(_))),
    recommend_cafe(Name),
    member(Name, ["Blumental", "Café Bravo"]),
    write('Test Case 2 Passed: Recommended Cafe is '), write(Name), nl.

%assume no preferences for any of the askables 
%the system shoulf recommend any cafe
test_case_3 :-
    retractall(askable(_)),
    assert(askable(budget(_))), 
    assert(askable(distance(_, _, _))),
    assert(askable(wifi(_))),
    assert(askable(work(_))),
    assert(askable(vegan(_))),
    assert(askable(card_payment(_))),
    assert(askable(size(_))),
    assert(askable(closed_days(_))),
    recommend_cafe(Name),
    cafe(Name, _, _, _, _, _, _, _, _, _, _, _), 
    write('Test Case 3 Passed: Recommended Cafe is '), write(Name), nl.

'''
