import express, { Request, Response } from 'express';

const app = express();
app.use(express.json());

// Route 1: path param with parseInt type inference
app.get('/users/:id', (req: Request, res: Response) => {
  const id = parseInt(req.params.id);
  res.json({ id });
});

// Route 2: query params with `as number` cast
app.get('/products', (req: Request, res: Response) => {
  const page = req.query.page as number;
  const limit = req.query.limit as number;
  const search = req.query.search as string;
  res.json({ page, limit, search });
});

// Route 3: body params with typed destructuring
app.post('/orders', (req: Request, res: Response) => {
  const { productId, quantity, price }: { productId: string; quantity: number; price: number } = req.body;
  res.json({ productId, quantity, price });
});

// Route 4: Request<Params, ResBody, Body, Query> generic
app.put('/items/:id', (req: Request<{ id: string }, any, { name: string; active: boolean }>, res: Response) => {
  const name = req.body.name;
  const active = req.body.active;
  res.json({ id: req.params.id, name, active });
});

// Route 5: plain JS-style (no type hints) — should still work
app.delete('/items/:id', (req, res) => {
  const id = req.params.id;
  res.sendStatus(204);
});

app.listen(3000);
