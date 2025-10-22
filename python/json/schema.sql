create table test
(
    id   serial primary key,
    data jsonb
);

insert into test(id, data)
values (1, '[{ "id": 1, "item": "keyboard", "price": 49.99 }, { "id": 2, "item": "mouse", "price": 19.99 }]'::JSONB),
       (2, '[{"id": 1001, "item": "lamp", "price": 399.46}, {"id": 1002, "item": "mouse", "price": 434.49}]'::JSONB),
       (3, '[]'::JSONB),
       (4, NULL);

insert into test(id, data)
values (2, '{}'::JSONB);
